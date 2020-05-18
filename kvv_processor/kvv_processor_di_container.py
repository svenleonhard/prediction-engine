from kvv_processor.helper.time_parser import TimeParser
from kvv_processor.travel_time_calculation import TravelTimeCalculator
from kvv_processor.repositories.trip_repository import TripRepository
from kvv_processor.repositories.route_repository import RouteRepository
from kvv_processor.repositories.stop_time_repository import StopTimeRepository
from kvv_processor.repositories.stop_repository import StopRepository
from kvv_processor.repositories.trip_section_repository import TripSectionRepository
from kvv_processor.repositories.neo_stop_repository import NeoStopRepository
from kvv_processor.repositories.line_repository import LineRepository
from kvv_processor.repositories.stop_journey_repository import StopJourneyRepository
from kvv_processor.repositories.station_repository import StationRepository
from kvv_processor.repositories.weather_repository import WeatherRepository
from kvv_processor.neo_stop_mapper import NeoStopMapper
from database.connection import Connection
from database.database import Database

import dependency_injector.containers as containers
import dependency_injector.providers as providers


class KvvProcessorDIContainer(containers.DeclarativeContainer):

    history_connection = providers.Factory(Connection,
                                               database='remote',
                                               schema='kvvhistory')
    history_session = providers.Factory(Database,
                                            connection=history_connection)

    trip_repository = providers.Factory(TripRepository,
                                        session=history_session)
    route_repository = providers.Factory(RouteRepository,
                                         session=history_session)
    stop_time_repository = providers.Factory(StopTimeRepository,
                                             session=history_session)
    trip_section_repository = providers.Factory(TripSectionRepository,
                                                session=history_session)
    stop_repository = providers.Factory(StopRepository,
                                        session=history_session)
    line_repository = providers.Factory(LineRepository,
                                        session=history_session)
    stop_journey_repository = providers.Factory(StopJourneyRepository, session=history_session)
    station_repository = providers.Factory(StationRepository, session=history_session)
    weather_repository = providers.Factory(WeatherRepository, session=history_session)

    time_parser = providers.Factory(TimeParser)
    travel_time_calculator = providers.Factory(
        TravelTimeCalculator,
        trip_repository=trip_repository,
        route_repository=route_repository,
        stop_time_repository=stop_time_repository,
        trip_section_repository=trip_section_repository,
        stop_repository=stop_repository,
        time_parser=time_parser)

    neo_connection = providers.Factory(Connection,
                                                   database='remote',
                                                   schema='kvv_history_new')
    neo_session = providers.Factory(
        Database, connection=neo_connection)
    neo_stop_repository = providers.Factory(NeoStopRepository,
                                            session=neo_session)
    neo_stop_mapper = providers.Factory(NeoStopMapper)
