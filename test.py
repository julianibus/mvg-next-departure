from mvg import MvgApi, TransportType

station = MvgApi.station('Himmelsschlüsselstraße, München')
print(station)
if station:
    mvgapi = MvgApi(station['id'])
    departures = mvgapi.departures(
        limit=3,
        offset=5,
        transport_types=[TransportType.UBAHN])
    print(station, departures)