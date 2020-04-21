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


# TODO New Releases
# if token:
#     sp = spotipy.Spotify(auth=token)
#     new_releases = sp.new_releases()
#     for item in new_releases['albums']['items']:
#         pprint.pprint(item)
#
# else:
#     print("Can't get token for", username)


# TODO: Get artist URI/detail
if token:
    sp = spotipy.Spotify(auth=token)
    nameOfArtist = 'Craig Xen'
    search_artist = sp.search(nameOfArtist, type='artist')
    # pprint.pprint(artist)  # prints out artist Drake details (shows multiple Drakes)
    # pprint.pprint(artist['artists']['items'][0]['uri'])  # gets URI of first item (the one we want)
    artist_uri = search_artist['artists']['items'][0]['uri']  # artist URI of first item (the one we want)
    # artist = sp.artist(artist_uri)  # obtained Artist through URI
    artist_catalog = sp.artist_albums(artist_uri)
    # pprint.pprint(artist_catalog['items'][0]['release_date'])  # gets first item's release date info
    # pprint.pprint(artist_catalog)  # gets first item's release date info

    # TODO Gets Album name and Release Date, finds latest release, outputs the latest Album name
    date_dict = {}
    date_list = []
    for item in artist_catalog['items']:
        date_list.append(item['release_date'])
        date_dict[item['release_date']] = item['name']

    print()

    max_date = max(date_list)
    print(date_dict.get(max_date))

else:
    print("Can't get token for", username)