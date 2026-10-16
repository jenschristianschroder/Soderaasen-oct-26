# Söderåsen · Sunday 18 October 2026

An interactive, static hiking planner for two friends travelling from Dollerupvej 7, Kastrup to Skäralid and back. Built for GitHub Pages, with no backend or API key.

## Default day

The planner opens with the requested 09:30 trail start and 6 km/h base walking pace, plus ascent allowance and 45 minutes of breaks. The optimizer runs only when you press its button; opening the page or refreshing weather preserves these defaults.

| Event | CEST |
| --- | --- |
| Leave Kastrup via the Øresund Bridge | 07:35 |
| Arrive at Skäralid | 09:15 |
| Start hiking | 09:30 |
| Final third begins | 12:51 |
| Finish the loop | 14:02 |
| Leave the park | 14:17 |
| Home, including 20-minute contingency | 16:17 |

These times are estimates. The page recomputes them from controls and the selected weather source. At the default pace and start time, the ferry option gives an estimated 06:50 departure and 17:02 return, including contingency. A 6 km/h base pace is ambitious on uneven trails; lower it if the terrain slows you down. Travel estimates are not traffic or ferry booking data.

## Features

- Full 2,994-point GPX loop: 17.321 km and approximately 538 m accumulated ascent.
- Interactive Leaflet/OpenStreetMap map, colored by arrival-time forecast; fully offline route-only SVG view.
- Distance scrubber, elevation profile, checkpoint weather table and hourly outlook.
- Bridge/ferry comparison, editable drive allowances, pace, breaks, start and return deadline.
- Start-time optimization focused on the final distance third, constrained by daylight and travel limits.
- Live Open-Meteo requests at five route samples. Refresh on opening, manually, and every 30 minutes while open.
- Saved forecast, local browser cache, clear source/retrieval labels and separately selectable attached forecast.
- Printable programme, original GPX download, navigation links and packing checklist.

## GitHub Pages

1. In **Settings → Pages → Build and deployment**, choose **GitHub Actions** as the source. This one-time repository setting needs owner/admin access; the deployment workflow token cannot enable a new Pages site itself.
2. The `Publish hiking planner` workflow tests and publishes the site on pushes to `main`. Use **Actions → Publish hiking planner → Run workflow** after first enabling Pages, or rerun a failed deployment.
3. The expected site address is `https://jenschristianschroder.github.io/Soderaasen-oct-26/`.

## Local use

Open `index.html` in a browser. The route data and saved forecasts load from local scripts; map tiles and fresh forecasts require an internet connection. Some browsers restrict external requests from local files; use GitHub Pages or a local static server in that case. The standalone `soderasen-trip.html` embeds all local dependencies and attachments for convenient sharing.

```sh
python3 -m http.server 8000
node --test tests/*.test.cjs
```

No build is needed. `template.html` is the editable page shell; copy it to `index.html` after shell edits. `build_standalone.py` assembles the optional single-file version. The workflow publishes `index.html` and `assets/` only.

## Timing and weather method

Distances are geodesic segment sums. Hiking minutes = distance / selected base pace × 60 + positive GPX ascent / 600 × 60 + breaks. One third of the break allowance is at 30% of the distance; the remainder is at 60%. GPX elevation is not independently surveyed and may contain noise. Stop locations are distance estimates, not named picnic facilities.

Forecast samples use 0%, 25%, 50%, 75% and 100% of route distance. Each point uses the nearest sample by route distance and the hour containing its estimated arrival. The first and last sample share coordinates; multiple points may share model grid cells. Ravines, tree cover and local exposure are not resolved. All schedule calculations use Stockholm/Copenhagen wall-clock minutes on 18 October 2026 (CEST), independent of the viewer's device timezone.

The optimizer evaluates 15-minute starts at eleven equally spaced points in the final third. Penalty = cloud cover × 0.1 + precipitation probability × 0.12 + precipitation mm × 40 + gust excess above 8 m/s × 1.5, with a 20-point wet-weather-code penalty. It chooses the earliest candidate within one point of the best score. It respects earliest departure, return deadline, sunrise and a 30-minute pre-sunset finish margin. This is a planning heuristic, not a probability of a pleasant walk.

The attachment has no visible provider, location, year or issue timestamp. It is treated as the user-provided forecast for the trip date. Missing quantities remain null. Blank rain entries are displayed as unspecified and add no amount penalty, rather than being presented as zero rainfall. Screenshot cloud icons get qualitative ranking values only for optimization; no cloud percentage is displayed as observed. Screenshot sunrise/sunset uses the stored API response.

Refresh failures, out-of-range dates and incomplete/null live data retain the last valid snapshot. The retrieval time is not a forecast model issue time. The app never substitutes a different day's data. Selecting the attachment keeps it selected even if a background refresh succeeds. A refresh does not change a manually chosen start; use the optimizer again.

## Verification

`node --test tests/*.test.cjs` checks route geometry, timing, break placement, spatial/hour mapping, missing forecast values, optimizer constraints, offline UI startup, controls and live-refresh caching using a minimal DOM harness. This does not replace visual browser testing. Full browser visual QA was unavailable in the creation environment.

## Sources and attribution

- Route: user-supplied `Söderåsen.gpx`, exported from AllTrails; preserved as `assets/route.gpx`.
- Attached forecast: `assets/forecast-reference.png`.
- [Open-Meteo](https://open-meteo.com/en/docs), weather data under CC BY 4.0. Exact request URL and retrieval time are in `assets/data.json`.
- [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors for basemap data.
- [Leaflet 1.9.4](https://leafletjs.com), BSD-2-Clause; license in `assets/leaflet-LICENSE.txt`.
- [Park entrances and parking](https://www.sverigesnationalparker.se/en/parks/soderasen-national-park/visit-the-park/getting-here/).
- [Øresund Bridge traffic](https://www.oresundsbron.com/en/traffic-information).
- [ØRESUNDSLINJEN timetable](https://www.oresundslinjen.com/timetable): crossing about 20 minutes. Check the operator for actual departures, check-in requirements and fares.
