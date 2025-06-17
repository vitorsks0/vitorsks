playlists={}
def criar_playlist():
    nome=input('Digite o nome da nova playlist:')
    if nome in playlists:
        print('Já existe uma playlist com esse nome.')
        return
    estilo=input('Digite o estilo musical das músicas que serão salvas nessa playlist:')
    playlists[nome] = {'estilo': estilo, 'musicas': []}
    print(f'Playlist "{nome}" criada com o estilo "{estilo}".')
