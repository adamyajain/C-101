import dropbox

class TransferData:
    def __init__(self, access_token)
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Ar4dR_cJnJY2P3lTN5FcnHA5UcDLCCeMA7fzcnrs4NQRMi_IxYGK5rH96AhH5hjMoVDtBiJ4-hQawWvvkyTVGZu8V_QPeav1mIHnT9ZHLJOAuomDsqN65yzyRu867kzPNo_j2JI'
    TransferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer :- ")
    file_to = input("Enter the full path to upload dropbox :- ")

    # API v2
    TransferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()    