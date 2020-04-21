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

# TODO: Get artist URI/detail
if token:
    sp = spotipy.Spotify(auth=token)

    # TODO [WORKS] Gets Album name and Release Date, finds latest release, outputs the latest Album name
    master_dict = {}
    artist_list = ['Craig Xen', 'Pouya', 'Playboy Carti', 'Lil Skies']

    for artist in artist_list:
        artist_dict = {}  # Key: Release Date, Value: Album Name
        date_list = []  # To be used to determine latest date (latest song released)
        artist_details = []
        search_artist = sp.search(artist, type='artist')
        artist_uri = search_artist['artists']['items'][0]['uri']  # Obtain artist URI number
        artist_catalog = sp.artist_albums(artist_uri)  # Obtain artist album full list

        for item in artist_catalog['items']:  # Iterating through ALL artist albums details
            # artist_name = item['artists'][0]['name']  # Artist Name
            date_list.append(item['release_date'])  # Adding all release date strings to date_list list
            artist_dict[item['release_date']] = item['name']  # artist_dict -> date: album name

        max_date = max(date_list)  # Latest Date
        latest_album_name = artist_dict.get(max_date)  # Obtains album name with latest release date
        artist_details.append(latest_album_name)  # adds latest album name to Artist Details list
        artist_details.append(max_date)  # adds latestvdate of album name to Artist Details list
        master_dict[artist] = artist_details  # artist name: artist_details list (album name, release date)

    for x, y in master_dict.items():
        print(x, y)
        print()

else:
    print("Can't get token for", username)