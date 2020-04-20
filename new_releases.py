import spotipy
import spotipy.util as util
import pprint


username = '1223672875'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
token = util.prompt_for_user_token(username,
                           scope,
                           client_id='dbf83f3fa8554986b5ce8e6a0ab700a5',
                           client_secret='b8091c597d894f4cb563ff833e007c17',
                           redirect_uri='https://google.com/')


# if token:
#     sp = spotipy.Spotify(auth=token)
#     new_releases = sp.new_releases()
#     for item in new_releases['albums']['items']:
#         pprint.pprint(item['artists'][0]['name'])  # prints out all the artist names one by one
#         pprint.pprint(item['name'])  # prints out all the artist title song/album names one by one
#         pprint.pprint(item['type'])  # prints out all the artist title song/album names one by one
#         print()
#
# else:
#     print("Can't get token for", username)

if token:
    sp = spotipy.Spotify(auth=token)
    new_releases = sp.new_releases()
    for item in new_releases['albums']['items']:
        pprint.pprint(item)

else:
    print("Can't get token for", username)