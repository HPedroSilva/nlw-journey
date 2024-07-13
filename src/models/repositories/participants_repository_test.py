import uuid

from src.models.settings.db_connection_handler import db_connection_handler

from src.models.repositories.participants_repository import ParticipantsRepository

db_connection_handler.connect()
participant_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())
emails_to_invite_id = str(uuid.uuid4())


def test_registry_participant():
    conn = db_connection_handler.get_connection()
    link_repository = ParticipantsRepository(conn)

    participant_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "Pedro",
    }

    link_repository.registry_participant(participant_infos)
