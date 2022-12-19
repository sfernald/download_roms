# download_roms
Threaded web scraping and download module written in python for web scraping and downloading game roms on Internet Archive

Internet Archive is the best and safest place to download legacy game roms such as old video game console roms. 

This application was designed to download all the rom links on a supplied Internet Archive page. So for example, there are functions to download all
US PS2 roms, PSP roms and PSX roms as examples. 

This script initially supports one download at a time, but then I implemented threading, so now you can specify the number of download threads to use
for much quicker downloads. 

It should be trivial to support the downloading of any other roms there on Internet Archive. If you want to download a group of pages, then look at the PS2
example which uses web scraping to download all the links from one Internet Archive user's page. 

