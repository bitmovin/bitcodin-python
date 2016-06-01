# bitcodin-python Changelog

## 0.4.0
* Implemented support for PlayReady and Widevine, both individually or combined

## 0.5.0
* Implemented support for HLS Encryption
* Added test for Multiple Audio Streams feature

## 1.0.0
* Implemented live stream support
* Added video_meta_data and extract_closed_captions functionality to job
* Added examples for DASH and HLS encryption
* Added additional error informations

## 1.0.1
* PEP8 style guide cosmetics

## 1.0.2
* Improved Live Stream example

## 1.0.3
* Improved Live Stream example

## 1.1.0
* Implemented vtt mpd support
* Added vtt mpd examples
* Implemented thumbnail support
* Added thumbnail examples
* Updated Live stream example

## 1.2.0
* Added support for deinterlacing jobs

## 1.2.2
* Refactored tests

## 1.2.3
* Removed BitcodinUnknownApiRequestUrlError and refactored tests 
* Updated examples

## 1.2.4
* Added audio merging feature example
* Added manifest info example

## 1.2.5
* Fixed wrong api base url

## 1.2.6
* Adjusted endpoint url

## 1.3.0
* Improved to_json() method for better debugging
* Added fairplay hls encryption job support
* Added create job skip analysis
* Adjusted examples

## 1.3.1
* Added example to show how to use start time and duration

## 1.4.0
* Improved camel case to snake case conversion (Fixed wrong conversion of lists)
* Adjusted tests to wait for jobs to finish
* Added some tests

## 1.4.1
* Fixed bug that to_json() converts BitcodinObject to dict

## 1.4.2
* Fixed wrong conversion of int and float of dictionary

## 1.4.3
* Fixed wrong conversion of int and float with python 2.7 support
* Added list_transfer_jobs() method
* Adjusted tests and example

## 1.4.4
* Changed to return object instead of boolean in transfer_job()

## 1.4.5
* Added flag create_sub_directory to outputs

## 1.4.6
* Changed preset to premium
* Adjusted encoding profile quality o examples

## 1.4.7
* Added keep aspect ratio feature and test

## 1.4.8
* Added basic authentication
* Added sftp output
* Added ftp input
* Added repr to BitcodinObject base class
* Removed testtools from setup.py

## 1.5.0
* Added transmux support
* Added transmux example

## 1.6.0
* Added get_thumbnail() method
* Thumbnail generation call now asynchronous

## 1.6.1
* Updated version names

## 1.6.2
* Added delete job method

## 1.6.5
* Fixed tests

## 1.6.6
* Updated readme