import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

class SpotifyController:
    def __init__(self):
        clientID = os.getenv("SPOTIFY_CLIENT_ID")
        clientSecret = os.getenv("SPOTIFY_CLIENT_SECRET")
        redirect_uri = "http://localhost:8888/callback"

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=clientID,
            client_secret=clientSecret,
            redirect_uri=redirect_uri,
            scope="user-modify-playback-state user-read-playback-state playlist-read-private user-library-read",
        ))

    def pause(self):
        self.sp.pause_playback()
    
    def play(self):
        self.sp.start_playback()

    def skip(self):
        self.sp.next_track()

    def previous(self):
        self.sp.previous_track()

    def go_to_start(self):
        self.sp.seek_track(0)
    
    def search_and_play(self, query):
        results = self.sp.search(query, limit=1)
        
        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            self.sp.start_playback(uris=[track_uri])
            return results['tracks']['items'][0]['name'] + " by " + results['tracks']['items'][0]['artists'][0]['name']

    def volume(self, volume):
        self.sp.volume(volume)

    def current_song(self):
        return self.sp.current_playback()

class SpotifyFunctions:
    def __init__(self):
        self.spotify = SpotifyController()

    def get_music_playing(self):
        try:
            track = self.spotify.current_song().get("item").get("name")
            artist = self.spotify.current_song().get("item").get("artists")[0].get("name")

            return {
                "track": track,
                "artist": artist
            }
        except Exception as e:
            return {"track": "Spotify Inactive", "artist": "Spotify Inactive"}
    
    def pause_music(self):
        try:
            self.spotify.pause()
            return {"success": True}
        except Exception as e:
            return {"success": False}

    def resume_music(self):
        try:
            self.spotify.play()
            return {"success": True}
        except Exception as e:
            return {"success": False}
    def search_and_play(self, query):
        try:
            return {
                "success": True,
                "playing": self.spotify.search_and_play(query)
            }
        except Exception as e:
            return {"success": False}
    def skip_music(self, skip_count=1):
        try:
            for _ in range(skip_count):
                self.spotify.sp.next_track()
            return {"success": True}
        except Exception as e:
            return {"success": False}
    def previous_music(self, skip_count=1):
        try:
            for _ in range(skip_count):
                self.spotify.previous()
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}
    def go_to_start_music(self):
        try:
            self.spotify.go_to_start()
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}
    def set_volume(self, volume):
        try:
            if 0 <= volume <= 100:
                self.spotify.volume(volume)
                return {"success": True}
            else:
                return {"success": False, "error": "Volume must be between 0 and 100."}
        except Exception as e:
            return {"success": False, "error": str(e)}
    def get_playlists(self):
        try:
            results = self.spotify.sp.current_user_playlists()
            
            playlists = [
                {"name": playlist['name'], "id": playlist['id']}
                for playlist in results['items']
            ]
            
            return {"success": True, "playlists": playlists}
        except Exception as e:
            return {"success": False, "error": str(e)}
    def play_playlist(self, playlist_name):
        try:
            results = self.spotify.sp.current_user_playlists()
            
            for playlist in results['items']:
                if playlist['name'].lower() == playlist_name.lower():
                    playlist_uri = playlist['uri']
                    
                    self.spotify.sp.start_playback(context_uri=playlist_uri)
                    
                    return {
                        "success": True,
                        "message": f"Playing playlist '{playlist['name']}'"
                    }
            return {
                "success": False,
                "message": f"Playlist '{playlist_name}' not found."
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error occurred: {e}"
            }