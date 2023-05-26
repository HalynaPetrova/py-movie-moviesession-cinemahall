from datetime import datetime
from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: datetime = None) -> MovieSession:
    queryset = MovieSession.objects.all()
    if session_date is not None:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int, ) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:

    update_dict = {"show_time": show_time,
                   "movie_id": movie_id,
                   "cinema_hall_id": cinema_hall_id}

    for field, value in update_dict.items():
        if value is not None:
            MovieSession.objects.filter(id=session_id).update(**{field: value})


def delete_movie_session_by_id(session_id: int) -> None:
    del_movie_session = MovieSession.objects.get(id=session_id)
    del_movie_session.delete()