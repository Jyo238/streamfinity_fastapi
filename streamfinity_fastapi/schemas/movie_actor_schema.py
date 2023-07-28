from datetime import date
from sqlmodel import Field, Relationship, SQLModel

class MovieInput(SQLModel):
    title: str
    length: int
    synopsis: str
    release_year: int
    director: str
    gene: str
    rating: int | None = None

class MovieActorLink(SQLModel, table=True):
    movie_id: int = Field(foreign_key="movie.id", primary_key=True, default=None)
    actor_id: int = Field(foreign_key="actor.id", primary_key=True, default=None)



class Movie(MovieInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    actors: list["Actor"] = Relationship(back_populates="movies",link_model=MovieActorLink)

class ActorInput(SQLModel):
    first_name: str
    last_name: str
    date_of_birth: date
    nationality: str
    biography: str | None = None
    profile_picture_url: str | None = None

class Actor(ActorInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    movies: list["Movie"] = Relationship(back_populates="actors", link_model=MovieActorLink)