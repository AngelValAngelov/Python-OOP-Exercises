from Desktop.python.python_oop.defining_classes_exercise.project.song import Song
from Desktop.python.python_oop.defining_classes_exercise.project.album import Album
from Desktop.python.python_oop.defining_classes_exercise.project.band import Band


if __name__ == "__main__":
    song = Song("Running in the 90s", 3.45, False)
    print(song.get_info())
    album = Album("Initial D", song)
    second_song = Song("Around the World", 2.34, False)
    print(album.add_song(second_song))
    print(album.details())
    print(album.publish())
    band = Band("Manuel")
    print(band.add_album(album))
    print(band.remove_album("Initial D"))
    print(band.details())
