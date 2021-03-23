Data was collected once per day (with days missing) over the course of the past few months.

### Reading the Data
Data can be downloaded or read directly from GitHub like so;
```python
import pandas as pd

pd.read_parquet('https://github.com/gumdropsteve/datasets/raw/master/airbnb/las_vegas.parquet')
```

Simply copy the file's URL and replace `/blob/` with `/raw/`.
- e.g. `https://github.com/gumdropsteve/datasets/blob/master/airbnb/las_vegas.parquet` -> `https://github.com/gumdropsteve/datasets/raw/master/airbnb/las_vegas.parquet`

### Collection Method
- Data was scraped once per day at various times
  - This was done in parallel with dask.delayed
  - You can find the scrape here: [gumdropsteve/airbnb/blob/main/01_scrape.py](https://github.com/gumdropsteve/airbnb/blob/main/01_scrape.py)
- Different `search_filter`s were used on each location to maxamize the number of views of that location
  - There are 8 possible options here
    - `''` - none - just searching the location
    - `'super_hosts'` - super hosts only
    - `'entire_homes'` - entire homes only
    - `'entire_home_super_hosts'` - entire home super hosts only 
    - `'hotel_rooms'` - hotel rooms only
    - `'hotel_room_super_hosts'` - hotel room super hosts only
    - `'private_rooms'` - private rooms only
    - `'private_room_super_hosts'` - private room super hosts only
    - `'shared_rooms'` - shared rooms only
    - `'shared_room_super_hosts'` - shared room super hosts only

  - Each `search_filter` was run each day unless there was a runtime error in which case the search filters that were processes were run and those that were still to be processed were not (this is because the check for "was this location recorded yet today?" is done via one the `ds` column and whether or not specific `search_filter` options have been recorded) 
- Bool columns note: bool columns are extracted from possible listed amenities. if the property does have one of the amenities, but it is not listed by the AirBnb host, the column here will show `False`.

### Data Dictionary
- ds: datetime the info was pulled
- search_filter: search filter applied on top of the city filter (None = no search filter)
- url: listing url
- title: listing title
- type: listing type
- location: listing location
- guests: number of guests the listing is for
- bedrooms: number of bedrooms the listing offers
- beds: number of beds the listing offers
- is_studio: (bool) is the listing a studio (studio apartment)?
- baths: number of baths the listing offers
- half_baths: number of half-baths the listing offers (missing probably means None)
- shared_baths: number of shared baths the listing offers (missing probably means None)
- price: (target) nightly price in $USD
- avg_rating: average rating by guests (missing could mean None)
- n_reviews: number of reveiws by guests (missing could mean None)
- gym_bool: is there a gym?
- wifi_bool: is there wifi?
- self_check_in_bool: is there self check-in?
- air_conditioning_bool: is there air conditioning?
- pets_allowed_bool: are pets allowed?
- indoor_fireplace_bool: is there an indoor fireplace?
- hot_tub_bool: is there a hot tub?
- free_parking_bool: is there free parking?
- pool_bool: is there a pool?
- kitchen_bool: is there a kitchen?
- breakfast_bool: is there breakfast?
- elevator_bool: is there an elevator?
- washer_bool: is there a washer?
- dryer_bool: is there a dryer?
- heating_bool: is there heating?
- waterfront_bool: is this listing on the waterfront?
- dishwasher_bool: is there a dishwasher?
- beachfront_bool: is this listing on the beachfront?
- ski_in_ski_out_bool: is there ski-in-ski-out? (snow skiing)
- terrace_bool: is there a terrace?
- sonos_sound_system_bool: is there a sonos sound system?
- bbq_grill_bool: is there a barbeque?
- hair_dryer_bool: is there a hair dryer?
- chefs_kitchen_bool: is there a chef's kitchen?
- wet_bar_bool: is there a wet bar? 
- sun_loungers_bool: sun loungers? 
- home_theater_bool: is there a home theater?
- housekeeping_bool: is housekeeping offered?
- gated_property_bool: is this a gated property?
- gas_fireplace_bool: is there a gas fireplace? 
- plunge_pool_bool: is there a plunge pool?
- infinity_pool_bool: is there an infiniti pool?
- sun_deck_bool: is there a sun deck? 
- game_room_bool: is there a game room?
- surround_sound_system_bool: is there a surround sound system?
- resort_access_bool: is there resort access? (often this means free access to resort)
