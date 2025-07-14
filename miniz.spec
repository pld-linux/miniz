Summary:	Implementation of the zlib and deflate compressed data format
Summary(pl.UTF-8):	Implementacja formatu danych z kompresją zlib i deflate
Name:		miniz
Version:	3.0.2
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/richgel999/miniz/releases
Source0:	https://github.com/richgel999/miniz/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a2fc179d5a5bcdcac42039829172dfc3
Patch0:		%{name}-libdir.patch
URL:		https://github.com/richgel999/miniz
BuildRequires:	cmake >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Miniz is a lossless, high performance data compression library in a
single source file that implements the zlib (RFC 1950) and deflate
(RFC 1951) compressed data format specification standards. It supports
the most commonly used functions exported by the zlib library, but is
a completely independent implementation so zlib's licensing
requirements do not apply. Miniz also contains simple to use functions
for writing .PNG format image files and reading/writing/appending .ZIP
format archives. Miniz's compression speed has been tuned to be
comparable to zlib's, and it also has a specialized real-time
compressor function designed to compare well against fastlz/minilzo.

%description -l pl.UTF-8
Miniz to biblioteka bezstratnej, szybkiej kompresji danych, zawarta w
pojedynczym pliku źródłowym, implementująca format danych zgodny ze
specyfikacją zlib (RFC 1950) oraz deflate (RFC 1951). Obsługuje
najczęściej używaną funkcjonalność biblioteki zlib, ale jest w pełni
niezależną implementacją, więc nie dotyczą jej wymagania licencyjne
biblioteki zlib. Miniz zawiera także proste w użyciu funkcje do
zapisu plików obrazów .PNG oraz odczytu/zapisu/dołączania do archiwów
w formacie .ZIP. Szybkość kompresji miniz jest porównywalna ze zlibem,
ma także specjalizowaną funkcję kompresji czasu rzeczywistego, nieźle
wypadającą w porównaniu z fastlz/minilzo.

%package devel
Summary:	Header files for miniz library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki miniz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for miniz library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki miniz.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog.md LICENSE readme.md
%attr(755,root,root) %{_libdir}/libminiz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libminiz.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libminiz.so
%{_includedir}/miniz
%{_libdir}/cmake/miniz
%{_pkgconfigdir}/miniz.pc
