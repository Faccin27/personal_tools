import spotipy
from spotipy.oauth2 import SpotifyOAuth

def transferir_musicas_entre_playlists(playlist_origem_id, playlist_destino_id):
    """
    Transfere todas as músicas de uma playlist do Spotify para outra playlist existente.
    
    Args:
        playlist_origem_id: ID da playlist de origem
        playlist_destino_id: ID da playlist de destino
    """
    
    scope = "playlist-read-private playlist-modify-private playlist-modify-public"
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope,
        client_id="clientid",
        client_secret="secret",
        redirect_uri="http://localhost:8888/callback"
    ))
    
    resultados = sp.playlist_items(playlist_origem_id)
    musicas = resultados['items']
    
    while resultados['next']:
        resultados = sp.next(resultados)
        musicas.extend(resultados['items'])
    
    ids_musicas = [item['track']['id'] for item in musicas if item['track'] is not None]
    
    tamanho_lote = 100
    
    for i in range(0, len(ids_musicas), tamanho_lote):
        lote = ids_musicas[i:i + tamanho_lote]
        sp.playlist_add_items(playlist_destino_id, lote)
        print(f"Adicionado lote de {len(lote)} músicas à playlist de destino")
    
    print(f"Transferência concluída! {len(ids_musicas)} músicas transferidas com sucesso.")

if __name__ == "__main__":
    PLAYLIST_ORIGEM_ID = "idold"
    PLAYLIST_DESTINO_ID = "idnew"
    
    transferir_musicas_entre_playlists(PLAYLIST_ORIGEM_ID, PLAYLIST_DESTINO_ID)