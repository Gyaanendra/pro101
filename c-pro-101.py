import dropbox


class Transferdata:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload(self, filefrom, file_to):
        # to upload files to dropbox
        dbx = dropbox.Dropbox(self.access_token)

        with open(filefrom, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    fi = input("enter your file name :")
    access_token= ""
    file = Transferdata(access_token)
    filefrom = fi
    file_to = "/pro101/"+filefrom
    file.upload(filefrom, file_to)

if __name__ == '__main__':
    main()
