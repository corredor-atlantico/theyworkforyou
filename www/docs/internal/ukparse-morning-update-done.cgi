#!/usr/bin/perl -w

use strict;
use FindBin;
use lib "$FindBin::Bin/../../../../perllib";

use mySociety::CGIFast;
use mySociety::Config;

mySociety::Config::set_file("$FindBin::Bin/../../conf/general");

my $path = '/data/vhost/' . mySociety::Config::get('DOMAIN');

while (my $q = new mySociety::CGIFast()) {
    my $pid = fork;
    if (not defined $pid) {
        print "Content-Type: text/plain\r\n\r\nFork failed";
    } elsif ($pid == 0) {
        exec "$path/mysociety/twfy/scripts/morningupdate";
    } else {
        print <<EOF;
Content-Type: text/plain

TheyWorkForYou morning update job scheduled.
EOF
        if ($q->path_info() eq "/0") {
            print "ukparse-morning-update-done.cgi: There were no scraper/parse errors\n";
        }
    }
}

