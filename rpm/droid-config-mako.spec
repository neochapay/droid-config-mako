# These and other macros are documented in ../droid-configs-device/droid-configs.inc

%define device mako
%define vendor lge

%define vendor_pretty LG
%define device_pretty Nexus 4

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 1.25

# We assume most devices will
%define have_modem 1

# this allows us to disable 4G on mako through config in sparse
Provides: ofono-configs
Obsoletes: ofono-configs-mer

Provides: bluez-configs
Obsoletes: bluez-configs-sailfish

Provides: obexd-configs
Obsoletes: obexd-configs-sailfish

%include droid-configs-device/droid-configs.inc

