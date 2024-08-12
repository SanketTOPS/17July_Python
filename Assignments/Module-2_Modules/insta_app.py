import instaloader

insta_id=input("Enter any Instagram ID:")

insta=instaloader.Instaloader()
insta.download_profile(insta_id)

print("Download Successfully!")