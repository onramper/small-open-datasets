# Small Open Datasets
> A collection of automatically-updated, ready-to-use and open-licensed datasets

## Dataset list
- [Currency Icons](./currency-icons): Icons for all circulating currencies in the world, generated from Wikipedia data
- [Base64 Cryptocurrency Icons](./base64-cryptocurrency-icons): A collection of base64-encoded cryptocurrency icons
- [Country Name to ISO Code Converter](./country-name-to-iso-code): A simple web utility to mass convert country names to their equivalent ISO3166 codes
- [ISO 3166 Alpha Code Converter](./iso3166-alpha-converter): Convert between alpha2 ('us') and alpha3 ('USA') ISO 3166 country codes

## Why use these packages
There are tons of projects on the internet that also provide this same data, however I haven't been able to find any project that checks all these boxes:
- [x] Is up to date
- [x] Is exhaustive
- [x] Is correct
- [x] Provides licensing information on the data or states the source of the data

This project attempts to tick all of these requirements by:
- Providing the source of the dataset, along with complete licensing information
- Establish weekly CI jobs that update the packages with the latest information and send notifications if anything breaks
- Make sure that the source is kept up to date
- Include only datasets that have permissive licenses

Furthermore, I've included extra nice-to-have things for many of the datasets, such as pre-rendered currency symbols, which can be used to display a symbol that is not supported by the system font.

## Licensing
Everything on this repo has been written directly by me and is under the MIT license, but the npm packages or websites generated using the code from this repo include data from external sources, which have different licenses.

More concretely, most of that data is under the Creative Commons Attribution-ShareAlike 3.0 Unported License (CC BY-SA) license, the one used by wikipedia which allows anyone to do whatever you want with the data as long as you provide proper attribution.

For data that is not under that license, I've made sure that it's license is permissive (eg: all allow commercial use) and can be considered open, but the specific details about each one can be found on the directory of each package.
