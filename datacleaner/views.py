from django.shortcuts import render

from .forms import DataForm

from django.contrib import messages

import pandas as pd

from django.conf import settings

from io import StringIO
import boto3

def index_view(request):
    context = {'form':DataForm()}
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            clean_null = form.cleaned_data.get('clean_null')
            filling = form.cleaned_data.get('filling')
            clean_duplicate = form.cleaned_data.get('clean_duplicate')
            bucket = settings.AWS_STORAGE_BUCKET_NAME
            csv_buffer = StringIO()
            csv_file = request.FILES['upload']
            context['file'] = csv_file
            csv_file.seek(0)
            df = pd.read_csv(csv_file, index_col=0)
            form.save()
            if clean_null == '1':
                df.dropna(inplace=True)
                if clean_duplicate == 1:
                    df.drop_duplicates(inplace=True)
                    df.to_csv(csv_buffer)
                    s3_resource = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
                    s3_resource.Object(bucket, 'data/output.csv').put(Body=csv_buffer.getvalue())
                else:
                    df.to_csv(csv_buffer)
                    s3_resource = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
                    s3_resource.Object(bucket, 'data/output.csv').put(Body=csv_buffer.getvalue())

            elif clean_null == '0':
                df.fillna(filling, inplace=True)
                if clean_duplicate == 1:
                    df.drop_duplicates(inplace=True)
                    df.to_csv(csv_buffer)
                    s3_resource = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
                    s3_resource.Object(bucket, 'data/output.csv').put(Body=csv_buffer.getvalue())
                else:
                    df.to_csv(csv_buffer)
                    s3_resource = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
                    s3_resource.Object(bucket, 'data/output.csv').put(Body=csv_buffer.getvalue())

            elif clean_duplicate == 1:
                df.drop_duplicates(inplace=True)
                df.to_csv(csv_buffer)
                s3_resource = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
                s3_resource.Object(bucket, 'data/output.csv').put(Body=csv_buffer.getvalue())

        else:
            messages.error(request, "Please submit only the correct file types!")
    else:
        form = DataForm()
    return render(request, 'datacleaner/index.html', context)
