from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name in [a.name for a in self.albums]:
            if album_name in [a.name for a in self.albums if a.published]:
                return "Album has been published. It cannot be removed."
            a = [a for a in self.albums if a.name == album_name][0]
            self.albums.remove(a)
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        result += '\n'.join([f"{a.details()}" for a in self.albums])
        return result