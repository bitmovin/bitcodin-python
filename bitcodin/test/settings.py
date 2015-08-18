__author__ = 'David Moser <david.moser@bitmovin.net>'

'''
Test configuration file
'''

api_key = '3f0c6d93c4fa8569dff63c295f980964ada5c1d9489aeb55978e61642d38fac1'
#api_key = 'e0da47bcb565f6573e26f0624990f6ad8b876d4f0c5cd31467bdbe65735e5387'
#api_key = '253afc1466f139e6c40bb486fffe55206a859f8fc81a5fee92c713e33df15209'

aws_config = {
    'access_key': 'AKIAJLWWP7E5MYNGERSA',
    'secret_key': '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',
    'host': 's3-eu-west-1.amazonaws.com',
    'name': 'bitcodin-ci-s3',
    'bucket': 'bitcodin-ci',
    'region': 'eu-west-1',
    'prefix': 'bitcodin-python'
}

ftp_config = {
    'host': 'ftp.bitcodin.com/content',
    'username': 'bitcodin-python',
    'password': 'xa9834ty'
}
