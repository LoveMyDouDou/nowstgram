#coding=utf-8
import os

from nowstagram import app
from qiniu import Auth,put_stream


# access_key=app.config['QINIU_ACCESS_KEY']
# secret_key=app.config['QINIU_SECRET_KEY']
#
# q=Auth(access_key,secret_key)
#
# bucket_name=app.config['QINIU_BUCKET_NAME']
#
#
# def qiniu_upload_file(source_file,save_file_name):
#     token=q.upload_token(bucket_name,save_file_name)
#     ret,info=put_stream(token,save_file_name,source_file.stream,
#                         "qiniu",os.fstat(source_file.stream.fileno()).st_size)
#     return None