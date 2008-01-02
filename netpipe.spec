%define real_name NetPIPE
%define name        netpipe
%define version	    3.7.1
%define release     %mkrel 1

Summary: Protocol independent performance tool
Name: %name
Version: %version
Release: %release
License: GPL
Group: Networking/Other
URL: http://www.scl.ameslab.gov/netpipe/
Source: http://www.scl.ameslab.gov/netpipe/code/%{real_name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
NetPIPE is a protocol independent performance tool that visually represents
the network performance under a variety of conditions. It performs simple
ping-pong tests, bouncing messages of increasing size between two processes,
whether across a network or within an SMP system. Message sizes are chosen
at regular intervals, and with slight perturbations, to provide a complete
test of the communication system. Each data point involves many ping-pong
tests to provide an accurate timing. Latencies are calculated by dividing
the round trip time in half for small messages ( < 64 Bytes ). 

%prep
%setup -q -n %{real_name}-%{version}

%build
%make memcpy tcp 

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 NPmemcpy %{buildroot}%{_bindir}/NPmemcpy
%{__install} -D -m0755 NPtcp %{buildroot}%{_bindir}/NPtcp
%{__install} -D -m0644 dox/netpipe.1 %{buildroot}%{_mandir}/man1/netpipe.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
# not in package as they requires gnupot and csh
%doc bin/*
%doc dox/README dox/*pdf 
%{_mandir}/man1/netpipe.1*
%{_bindir}/*


