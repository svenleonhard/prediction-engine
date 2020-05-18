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

    historydata_connection = providers.Factory(Connection,
                                               database='local',
                                               schema='historydata')
    historydata_session = providers.Factory(Database,
                                            connection=historydata_connection)

    trip_repository = providers.Factory(TripRepository,
                                        session=historydata_session)
    route_repository = providers.Factory(RouteRepository,
                                         session=historydata_session)
    stop_time_repository = providers.Factory(StopTimeRepository,
                                             session=historydata_session)
    trip_section_repository = providers.Factory(TripSectionRepository,
                                                session=historydata_session)
    stop_repository = providers.Factory(StopRepository,
                                        session=historydata_session)
    line_repository = providers.Factory(LineRepository,
                                        session=historydata_session)
    stop_journey_repository = providers.Factory(StopJourneyRepository, session=historydata_session)
    station_repository = providers.Factory(StationRepository, session=historydata_session)


    time_parser = providers.Factory(TimeParser)
    travel_time_calculator = providers.Factory(
        TravelTimeCalculator,
        trip_repository=trip_repository,
        route_repository=route_repository,
        stop_time_repository=stop_time_repository,
        trip_section_repository=trip_section_repository,
        stop_repository=stop_repository,
        time_parser=time_parser)

    kvv_history_new_connection = providers.Factory(Connection,
                                                   database='remote',
                                                   schema='kvv_history_new')
    kvv_history_new_session = providers.Factory(
        Database, connection=kvv_history_new_connection)
    neo_stop_repository = providers.Factory(NeoStopRepository,
                                            session=kvv_history_new_session)
    neo_stop_mapper = providers.Factory(NeoStopMapper)

    kvvhistory_connection = providers.Factory(Connection,
                                                   database='remote',
                                                   schema='kvvhistory')
    kvvhistory_session = providers.Factory(
        Database, connection=kvvhistory_connection)
    
    weather_repository = providers.Factory(WeatherRepository, session=kvvhistory_session)

