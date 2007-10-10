# TODO:
#	- update desktop files, think about su-wrappers for console
#	- package web admin
#	- fix log file permissions
#
# Conditional build:
%bcond_without	console_wx	# wx-console program
%bcond_without	gnome		# gnome-console program
%bcond_without	sqlite		# use sqlite
%bcond_with	bat		# bat Qt4 GUI
%bcond_with	mysql		# use mysql
%bcond_with	pgsql		# use PostgreSQL
%bcond_with	python
%bcond_with	rescue
%bcond_with	sqlite3		# use sqlite3 insted sqlite
%bcond_with	sqlite3_sync_off	# makes sqlite3 backend much faster, but less reliable
%if %{with sqlite}
%define		_database	sqlite
%endif
%if %{with sqlite3}
%define		_database	sqlite3
%undefine       with_sqlite
%undefine       with_mysql
%undefine       with_pgsql
%endif
%if %{with pgsql}
%define		_database	postgresql
%undefine       with_sqlite
%undefine       with_sqlite3
%undefine       with_mysql
%endif
%if %{with mysql}
%define		_database	mysql
%undefine       with_sqlite
%undefine       with_sqlite3
%undefine       with_pgsql
%undefine       with_sqlite3_sync_off
%endif
#
Summary:	Bacula - The Network Backup Solution
Summary(pl.UTF-8):	Bacula - rozwiązanie do wykonywania kopii zapasowych po sieci
Name:		bacula
Version:	2.2.4
Release:	0.2
Epoch:		0
License:	extended GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/bacula/%{name}-%{version}.tar.gz
# Source0-md5:	2e3bbac3bf8b6d4c0825997c3009f18f
Source1:	http://dl.sourceforge.net/bacula/%{name}-docs-%{version}.tar.bz2
# Source1-md5:	115f7276ad5dda8060ac0f9595372cef
Source2:	http://dl.sourceforge.net/bacula/%{name}-rescue-2.2.4.tar.gz
# Source2-md5:	a5416d1e9ebd13af8e53f35e4d77bc3e
Source10:	%{name}-dir.init
Source11:	%{name}-fd.init
Source12:	%{name}-sd.init
Source13:	%{name}.logrotate
Source14:	%{name}-dir.sysconfig
Source15:	%{name}-fd.sysconfig
Source16:	%{name}-sd.sysconfig
Patch0:		%{name}-dvd-handler_path.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-compile.patch
Patch3:		%{name}-wx28.patch
Patch4:		%{name}-sqlite3_init_query.patch

Patch10:	%{name}-2.2.4-ansi-label.patch
Patch11:	%{name}-2.2.4-lost-block.patch
Patch12:	%{name}-2.2.4-parse-command.patch
Patch13:	%{name}-2.2.4-poll-mount.patch
Patch14:	%{name}-2.2.4-replace.patch
Patch15:	%{name}-2.2.4-restore.patch
Patch16:	%{name}-2.2.4-sd-auth-fail.patch
Patch17:	%{name}-2.2.4-sql.patch
Patch18:	%{name}-2.2.4-verify.patch

URL:		http://www.bacula.org/
BuildRequires:	acl-static
BuildRequires:	automake
%if %{with rescue}
BuildRequires:	fakeroot
%endif
BuildRequires:	glibc-static
%if %{with gnome}
BuildRequires:	libgnome-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
%endif
BuildRequires:	libstdc++-static
BuildRequires:	libwrap-static
BuildRequires:	mtx
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	openssl-static
BuildRequires:	pkgconfig
%if %{with python}
BuildRequires:	python-static
%endif
%if %{with bat}
BuildRequires:	qwt-devel
BuildRequires:	QtGui-devel
%endif
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
%{?with_sqlite3:BuildRequires:  sqlite3-devel}
%{?with_sqlite:BuildRequires:  sqlite-devel}
%{?with_mysql:BuildRequires:  mysql-devel}
%{?with_pgsql:BuildRequires:  postgresql-devel}
%if %{with console_wx}
BuildRequires:	wxGTK2-unicode-devel >= 2.4.0
%endif
BuildRequires:	zlib-devel
BuildRequires:	zlib-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}
%define		_localstatedir	/var/lib/%{name}

# dependency section is broken. ccache usage is instead to makefiles
%undefine	with_ccache

%description
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files.

%description -l pl.UTF-8
Bacula - przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Bacula to zbiór programów umożliwiających administratorowi na
zarządzanie kopiami zapasowymi, odzyskiwaniem i weryfikacją danych w
sieci komputerów różnego rodzaju. W terminologii technicznej jest to
program do kopii zapasowych pracujący w architekturze klient-serwer.
Bacula jest stosunkowo łatwa w użyciu i wydajna, oferując przy tym
wiele zaawansowanych możliwości przy zarządzaniu nośnikami,
ułatwiających znalezienie i odzyskanie utraconych lub uszkodzonych
plików.

%package common
Summary:	Common files for bacula package
Summary(pl.UTF-8):	Pliki wspólne dla pakietu bacula
Group:		Networking/Utilities
Requires(post):	openssl-tools
Requires(post):	sed >= 4.0
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Conflicts:	bacula-console < 0:1.34.6
Conflicts:	bacula-dir < 0:1.34.6
Conflicts:	bacula-fd < 0:1.34.6
Conflicts:	bacula-sd < 0:1.34.6

%description common
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files.

%description common -l pl.UTF-8
Bacula - przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Bacula to zbiór programów umożliwiających administratorowi na
zarządzanie kopiami zapasowymi, odzyskiwaniem i weryfikacją danych w
sieci komputerów różnego rodzaju. W terminologii technicznej jest to
program do kopii zapasowych pracujący w architekturze klient-serwer.
Bacula jest stosunkowo łatwa w użyciu i wydajna, oferując przy tym
wiele zaawansowanych możliwości przy zarządzaniu nośnikami,
ułatwiających znalezienie i odzyskanie utraconych lub uszkodzonych
plików.

%package dir
Summary:	Bacula Director and Catalog services
Summary(pl.UTF-8):	Usługi Bacula Director i Catalog
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Obsoletes:	bacula-updatedb

%description dir
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Director is the program that supervises all the backup,
restore, verify and archive operations. The system administrator uses
the Bacula Director to schedule backups and to recover files. Catalog
services are comprised of the software programs responsible for
maintaining the file indexes and volume databases for all files backed
up. The Catalog services permit the System Administrator or user to
quickly locate and restore any desired file, since it maintains a
record of all Volumes used, all Jobs run, and all Files saved. This
build requires sqlite%{?with_sqlite3:3} to be installed separately as the catalog
database.

%description dir -l pl.UTF-8
Bacula - przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Bacula Director to program nadzorujący wszystkie operacje wykonywania
kopii zapasowych, odzyskiwania, weryfikacji i archiwizowania.
Administrator używa Bacula Directora do szeregowania kopii zapasowych
oraz odzyskiwania plików. Usługi katalogowe (Catalog services) są
używane przez programy odpowiedzialne za zarządzanie indeksami plików
i bazą danych wolumenów dla wszystkich kopiowanych plików. Usługi
katalogowe umożliwiają administratorowi lub użytkownikowi szybko
zlokalizować i odtworzyć dowolny plik, ponieważ utrzymują rekord ze
wszystkimi używanymi wolumenami, uruchomionymi zadaniami i zapisanymi
plikami. Pakiet wymaga %{_database} zainstalowanego oddzielnie jako bazy
danych dla katalogu.

%package console
Summary:	Bacula Console
Summary(pl.UTF-8):	Konsola Baculi
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description console
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director. This is the text only console
interface.

%description console -l pl.UTF-8
Bacula - przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Bacula Console to program umożliwiający administratorowi lub
użytkownikowi komunikowanie się z programem Bacula Director. To jest
interfejs czysto tekstowy.

%package console-wx
Summary:	Bacula wxWidgets Console
Summary(pl.UTF-8):	Konsola Baculi oparta na wxWidgets
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description console-wx
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director. This is the wxWidgets GUI
interface.

%description console-wx -l pl.UTF-8
Bacula - przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Bacula Console to program umożliwiający administratorowi lub
użytkownikowi komunikowanie się z programem Bacula Director. To jest
interfejs graficzny oparty na wxWidgets.

%package console-gnome
Summary:	Bacula GNOME Console
Summary(pl.UTF-8):	Konsola Baculi oparta dla GNOME
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description console-gnome
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director. This is the GNOME GUI interface.

%description console-gnome -l pl.UTF-8
Bacula - przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Bacula Console to program umożliwiający administratorowi lub
użytkownikowi komunikowanie się z programem Bacula Director. To jest
interfejs graficzny oparty na GNOME.

%package tray-monitor
Summary:	Bacula Tray Monitor
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description tray-monitor
Bacula - It comes by night and sucks the vital essence from your
computers.

The Monitor program is typically an icon in the system tray. However,
once the icon is expanded into a full window, the administrator or
user can obtain status information about the Director or the backup
status on the local workstation or any other Bacula daemon that is
configured.

%package fd
Summary:	Bacula File services (Client)
Summary(pl.UTF-8):	Usługi Bacula File (klient)
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description fd
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula File services (or Client program) is the software program that
is installed on the machine to be backed up. It is specific to the
operating system on which it runs and is responsible for providing the
file attributes and data when requested by the Director. The File
services are also responsible for the file system dependent part of
restoring the file attributes and data during a recovery operation.
This program runs as a daemon on the machine to be backed up, and in
some of the documentation, the File daemon is referred to as the
Client (for example in Bacula configuration file).

%description fd -l pl.UTF-8
Bacula - przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Usługi Bacula File (inaczej program kliencki) to oprogramowanie, które
instaluje się na maszynach, z których mają być wykonywane kopie
zapasowe. Są one specyficzne dla systemu operacyjnego, pod którym
działa dana maszyna i odpowiadają za dostarczanie atrybutów i danych
plików na żądanie Directora. Usługi plikowe są także odpowiedzialne za
zależną od systemu plików część odzyskiwania atrybutów i danych plików
podczas operacji odzyskiwania danych. Program działa jako demon na
maszynie, która ma być backupowana i w części dokumentacji demon ten
(File) jest nazywany klientem (na przykład w pliku konfiguracyjnym
Baculi).

%package sd
Summary:	Bacula Storage services
Summary(pl.UTF-8):	Usługi Bacula Storage
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Conflicts:	dvd+rw-tools <= 5.21.4.10.8-1

%description sd
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Storage services consist of the software programs that perform
the storage and recovery of the file attributes and data to the
physical backup media or volumes. In other words, the Storage daemon
is responsible for reading and writing your tapes (or other storage
media, e.g. files). The Storage services runs as a daemon on the
machine that has the backup device (usually a tape drive).

%description sd -l pl.UTF-8
Bacula - przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Usługi Bacula Storage składają się z programów obsługujących
przechowywanie danych oraz odzyskiwanie atrybutów i danych na
fizycznych nośnikach lub wolumenach. Innymi słowy, demon Storage jest
odpowiedzialny za odczyt i zapis taśm (lub innych nośników do
przechowywania danych, np. plików). Usługi Storage działają jako demon
na maszynie, która zawiera urządzenie backupowe (zwykle napęd
taśmowy).

%package rescue
Summary:	Bacula - The Network Backup Solution
Summary(pl.UTF-8):	Bacula - rozwiązanie do wykonywania kopii zapasowych po sieci
Group:		Networking/Utilities
Requires:	%{name}-fd = %{epoch}:%{version}-%{release}
Requires:	coreutils
Requires:	util-linux

%description rescue
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files.

This package installs scripts for disaster recovery and builds rescue
floppy disk for bare metal recovery.

To make the bacula rescue disk run "./make_rescue_disk
--copy-static-bacula
- --copy-etc-files" from the %{_sysconfdir}/rescue directory. To
  recreate the rescue information for this system run ./getdiskinfo
  again.

%description rescue -l pl.UTF-8
Bacula - przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Bacula to zbiór programów umożliwiających administratorowi na
zarządzanie kopiami zapasowymi, odzyskiwaniem i weryfikacją danych w
sieci komputerów różnego rodzaju. W terminologii technicznej jest to
program do kopii zapasowych pracujący w architekturze klient-serwer.
Bacula jest stosunkowo łatwa w użyciu i wydajna, oferując przy tym
wiele zaawansowanych możliwości przy zarządzaniu nośnikami,
ułatwiających znalezienie i odzyskanie utraconych lub uszkodzonych
plików.

Ten pakiet zawiera skrypty do odtwarzania po awarii i tworzy dyskietkę
ratunkowe do odtwarzania systemu od zera.

Aby stworzyć dyskietkę ratunkową Baculi, należy uruchomić "./make_rescue_disk
--copy-static-bacula - --copy-etc-files" z katalogu
%{_sysconfdir}/rescue . Aby ponownie utworzyć informacje ratunkowe dla
danego systemu, należy ponownie uruchomić ./getdiskinfo .

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1

%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p0
%patch14 -p0
%patch15 -p0
%patch16 -p0
%patch17 -p0
%patch18 -p0


tar -xf %{SOURCE2} && ln -s bacula-rescue-* rescue
sed -i -e 's#wx-config#wx-gtk2-unicode-config#g' configure*
sed -i -e 's#-lreadline -lhistory -ltermcap#-lreadline -lhistory#g' configure*
sed -i -e 's#bindir=.*#bindir=%{_bindir}#g' \
	src/cats/create_* src/cats/delete_* src/cats/drop_* \
	src/cats/grant_* src/cats/make_* src/cats/update_*
sed -i -e 's/@hostname@/--hostname--/' src/*/*.conf.in

%build
cp -f %{_datadir}/automake/config.sub autoconf
CPPFLAGS="-I/usr/include/ncurses -I%{_includedir}/readline"
%configure \
	--with-scriptdir=%{_libexecdir}/%{name} \
	--%{!?with_gnome:dis}%{?with_gnome:en}able-gnome \
	%{?with_bat:--enable-bat} \
	--disable-conio \
	--enable-smartalloc \
	%{?with_console_wx:--enable-bwx-console} \
	--enable-tray-monitor \
	%{?with_python:--with-python} \
	--with-readline \
	--with-tcp-wrappers \
	--with-working-dir=%{_var}/lib/%{name} \
	--with-dump-email="root@localhost" \
	--with-job-email="root@localhost" \
	--with-smtp-host=localhost \
	--with-pid-dir=/var/run \
	--with-subsys-dir=/var/lock/subsys \
	--with-%{_database} \
	%{?with_sqlite3_sync_off:--enable-extra-sqlite3-init="pragma synchronous=0;"} \
	--with-dir-password="#FAKE-dir-password#" \
	--with-fd-password="#FAKE-fd-password#" \
	--with-sd-password="#FAKE-sd-password#" \
	--with-mon-dir-password="#FAKE-mon-dir-password#" \
	--with-mon-fd-password="#FAKE-mon-fd-password#" \
	--with-mon-sd-password="#FAKE-mon-sd-password#" \
	--with-openssl
%{__make}

%if %{with rescue}
cd rescue
%configure \
	--with-bacula=../
cd linux/cdrom
fakeroot %{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,pam.d,sysconfig}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/rescue
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_mandir},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# static daemon
#strip -R.comment -R.note src/filed/static-bacula-fd
#install src/filed/static-bacula-fd $RPM_BUILD_ROOT%{_sysconfdir}/rescue/bacula-fd

install %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-dir
install %{SOURCE11} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-fd
install %{SOURCE12} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-sd
install %{SOURCE13} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}-dir
install %{SOURCE14} $RPM_BUILD_ROOT/etc/sysconfig/bacula-dir
install %{SOURCE15} $RPM_BUILD_ROOT/etc/sysconfig/bacula-fd
install %{SOURCE16} $RPM_BUILD_ROOT/etc/sysconfig/bacula-sd

%if %{with console_wx}
# tray-monitor is for regular users
mv $RPM_BUILD_ROOT%{_sbindir}/bacula-tray-monitor $RPM_BUILD_ROOT%{_bindir}

install scripts/bacula.png $RPM_BUILD_ROOT%{_pixmapsdir}/bacula.png
install src/tray-monitor/generic.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/bacula-tray-monitor.xpm
install scripts/bacula.desktop.gnome2 $RPM_BUILD_ROOT%{_desktopdir}/bacula.desktop
sed -e 's/gnome-console/wx-console/g;s/Console/Wx Console/g' \
	scripts/bacula.desktop.gnome2 > $RPM_BUILD_ROOT%{_desktopdir}/bacula-wx.desktop
sed -e 's#%{_sbindir}#%{_bindir}#' \
	scripts/bacula-tray-monitor.desktop > $RPM_BUILD_ROOT%{_desktopdir}/bacula-tray-monitor.desktop
%endif

%if %{with rescue}
# install the rescue stuff, these are the rescue scripts
install rescue/linux/floppy/backup.etc.list $RPM_BUILD_ROOT%{_sysconfdir}/rescue
install rescue/linux/floppy/*_* $RPM_BUILD_ROOT%{_sysconfdir}/rescue
install rescue/linux/floppy/getdiskinfo $RPM_BUILD_ROOT%{_sysconfdir}/rescue
install rescue/linux/floppy/sfdisk.bz2 $RPM_BUILD_ROOT%{_sysconfdir}/rescue
%endif

# install the updatedb scripts
install updatedb/update_sqlite* $RPM_BUILD_ROOT%{_libexecdir}/%{name}

# place for site passwords
touch $RPM_BUILD_ROOT%{_sysconfdir}/{dir-password,fd-password,sd-password}
touch $RPM_BUILD_ROOT%{_sysconfdir}/{mon-dir-password,mon-fd-password,mon-sd-password}

# some file changes
rm -f $RPM_BUILD_ROOT%{_libexecdir}/%{name}/{gconsole,startmysql,stopmysql,bacula,bconsole,fd}
rm -f $RPM_BUILD_ROOT%{_sbindir}/static-bacula-fd
%if !%{with console_wx}
rm -f $RPM_BUILD_ROOT%{_desktopdir}/bacula-wx.desktop
%endif
touch $RPM_BUILD_ROOT%{_sysconfdir}/.pw.sed

%clean
rm -rf $RPM_BUILD_ROOT

%pre common
%groupadd -P %{name}-common -g 136 -r -f bacula
%useradd -P %{name}-common -u 136 -r -d /var/lib/bacula -s /bin/false -c "Bacula User" -g bacula bacula

%post common
echo "Updating bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	if [ ! -s $f ] ; then
		openssl rand -base64 33 > $f
	fi
	p=`cat $f`
	for cf in *.conf *.conf.rpmnew ; do
		[ -f $cf ] && sed -i -e"s:#FAKE-$f#:$p:" "$cf" || :
	done
done
for cf in *.conf *.conf.rpmnew ; do
	[ -f $cf ] && sed -i -e"s:--hostname--:`hostname`:" "$cf" || :
done

%postun common
if [ "$1" = "0" ]; then
	%userremove bacula
	%groupremove bacula
fi

%post dir
umask 077
[ -s %{_localstatedir}/bacula.db ] && \
	DB_VER=`echo "select * from Version;" | \
	%{_bindir}/sqlite%{?with_sqlite3:3} %{_localstatedir}/bacula.db | tail -n 1 2>/dev/null`
if [ -z "$DB_VER" ]; then
# grant privileges and create tables
	%{_libexecdir}/%{name}/grant_bacula_privileges > dev/null
	%{_libexecdir}/%{name}/create_bacula_database > dev/null
	%{_libexecdir}/%{name}/make_bacula_tables > dev/null
elif [ "$DB_VER" -lt "9" ]; then
	echo "Backing up bacula tables"
	echo ".dump" | sqlite%{?with_sqlite3:3} %{_localstatedir}/bacula.db | bzip2 > %{_localstatedir}/bacula_backup.sql.bz2
	echo "Upgrading bacula tables"
	%if %{with sqlite3}
		type=sqlite3
		if [ "$DB_VER" -lt "9" ]; then
			%{_libexecdir}/%{name}/update_${type}_tables_8_to_9
		fi
	%endif
	%if %{with sqlite}
		type=sqlite
		if [ "$DB_VER" -lt "9" ]; then
			if [ "$DB_VER" -lt "8" ]; then
				if [ "$DB_VER" -lt "7" ]; then
					if [ "$DB_VER" -lt "6" ]; then
						if [ "$DB_VER" -lt "5" ]; then
							%{_libexecdir}/%{name}/update_${type}_tables_4_to_5
						fi
						%{_libexecdir}/%{name}/update_${type}_tables_5_to_6
					fi
					%{_libexecdir}/%{name}/update_${type}_tables_6_to_7
				fi
				%{_libexecdir}/%{name}/update_${type}_tables_7_to_8
			fi
			%{_libexecdir}/%{name}/update_${type}_tables_8_to_9
		fi
	%endif
	%{_libexecdir}/%{name}/update_bacula_tables
	echo "If bacula works correctly you can remove the backup file %{_localstatedir}/bacula_backup.sql.bz2"
fi
chown -R bacula:bacula %{_localstatedir}
chmod -R u+rX,go-rwx %{_localstatedir}/*

echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew 2>/dev/null || :
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew 2>/dev/null || :

/sbin/chkconfig --add bacula-dir
%service bacula-dir restart "Bacula Director daemon"

%preun dir
if [ "$1" = "0" ]; then
	%service bacula-dir stop
	/sbin/chkconfig --del bacula-dir
fi

%post fd
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew 2>/dev/null || :
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew 2>/dev/null || :

/sbin/chkconfig --add bacula-fd
%service bacula-fd restart "Bacula File daemon"

%preun fd
if [ "$1" = "0" ]; then
	%service bacula-fd stop
	/sbin/chkconfig --del bacula-fd
fi

%post sd
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew 2>/dev/null || :
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew 2>/dev/null || :

/sbin/chkconfig --add bacula-sd
%service bacula-sd restart "Bacula Storage daemon"

%preun sd
if [ "$1" = "0" ]; then
	%service bacula-sd stop
	/sbin/chkconfig --del bacula-sd
fi

%pre console
if [ -e %{_sysconfdir}/console.conf -a ! -e %{_sysconfdir}/bconsole.conf ]; then
	mv %{_sysconfdir}/console.conf %{_sysconfdir}/bconsole.conf
fi

%post console
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew 2>/dev/null || :
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew 2>/dev/null || :

%post console-wx
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew 2>/dev/null || :
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew 2>/dev/null || :

%post console-gnome
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew 2>/dev/null || :
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew 2>/dev/null || :

%post tray-monitor
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew 2>/dev/null || :
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew 2>/dev/null || :

%post rescue
# link our current installed conf file to the rescue directory
ln -sf %{_sysconfdir}/bacula-fd.conf %{_sysconfdir}/rescue/bacula-fd.conf

# run getdiskinfo
echo "Creating rescue files for this system..."
cd %{_sysconfdir}/rescue
./getdiskinfo

%preun rescue
# remove the files created after the initial rpm installation
if [ "$1" = "0" ]; then
	rm -f %{_sysconfdir}/rescue/bacula-fd.conf
	rm -f %{_sysconfdir}/rescue/partition.*
	rm -f %{_sysconfdir}/rescue/format.*
	rm -f %{_sysconfdir}/rescue/mount_drives
	rm -f %{_sysconfdir}/rescue/start_network
	rm -f %{_sysconfdir}/rescue/sfdisk
	rm -rf %{_sysconfdir}/rescue/diskinfo/*
fi

%files common
%defattr(644,root,root,755)
%doc LICENSE
%dir %{_sysconfdir}
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*-password
%attr(755,root,root) %{_sbindir}/bsmtp
%attr(755,root,root) %{_sbindir}/btraceback
%{_mandir}/man8/bacula.8*
%{_mandir}/man1/bsmtp.1*
%{_mandir}/man8/btraceback.8*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/btraceback.dbx
%{_libexecdir}/%{name}/btraceback.gdb
%attr(770,root,bacula) %dir %{_localstatedir}

%files dir
%defattr(644,root,root,755)
%doc ChangeLog CheckList ReleaseNotes kernstodo LICENSE
#%doc examples %{name}-docs-%{version}/manual/{*.pdf,bacula}
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bacula-dir.conf
%ghost %{_sysconfdir}/.pw.sed
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/bacula-dir
%attr(754,root,root) /etc/rc.d/init.d/bacula-dir
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/bacula-dir
%attr(755,root,root) %{_sbindir}/bacula-dir
%attr(755,root,root) %{_sbindir}/bregex
%attr(755,root,root) %{_sbindir}/bwild
%attr(755,root,root) %{_sbindir}/dbcheck
%{_mandir}/man8/bacula-dir.8*
%{_mandir}/man8/dbcheck.8*
%{_libexecdir}/%{name}/query.sql
%if %{with sqlite3}
%attr(755,root,root) %{_libexecdir}/%{name}/create_sqlite3_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_sqlite3_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_sqlite3_tables
%attr(755,root,root) %{_libexecdir}/%{name}/grant_sqlite3_privileges
%attr(755,root,root) %{_libexecdir}/%{name}/make_sqlite3_tables
%attr(755,root,root) %{_libexecdir}/%{name}/update_sqlite3_*
%endif
%if %{with sqlite}
%attr(755,root,root) %{_libexecdir}/%{name}/create_sqlite_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_sqlite_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_sqlite_tables
%attr(755,root,root) %{_libexecdir}/%{name}/grant_sqlite_privileges
%attr(755,root,root) %{_libexecdir}/%{name}/make_sqlite_tables
%attr(755,root,root) %{_libexecdir}/%{name}/update_sqlite_*
%endif
%if %{with mysql}
%attr(755,root,root) %{_libexecdir}/%{name}/create_mysql_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_mysql_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_mysql_tables
%attr(755,root,root) %{_libexecdir}/%{name}/grant_mysql_privileges
%attr(755,root,root) %{_libexecdir}/%{name}/make_mysql_tables
%attr(755,root,root) %{_libexecdir}/%{name}/update_mysql_*
%endif
%if %{with pgsql}
%attr(755,root,root) %{_libexecdir}/%{name}/create_postgresql_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_postgresql_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_postgresql_tables
%attr(755,root,root) %{_libexecdir}/%{name}/grant_postgresql_privileges
%attr(755,root,root) %{_libexecdir}/%{name}/make_postgresql_tables
%attr(755,root,root) %{_libexecdir}/%{name}/update_postgresql_*
%endif
%attr(755,root,root) %{_libexecdir}/%{name}/create_bacula_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_bacula_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_bacula_tables
%attr(755,root,root) %{_libexecdir}/%{name}/grant_bacula_privileges
%attr(755,root,root) %{_libexecdir}/%{name}/make_bacula_tables
%attr(755,root,root) %{_libexecdir}/%{name}/update_bacula_tables
%attr(755,root,root) %{_libexecdir}/%{name}/make_catalog_backup
%attr(755,root,root) %{_libexecdir}/%{name}/delete_catalog_backup

%files fd
%defattr(644,root,root,755)
%doc LICENSE
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bacula-fd.conf
%attr(754,root,root) /etc/rc.d/init.d/bacula-fd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/bacula-fd
%attr(755,root,root) %{_sbindir}/bacula-fd
%{_mandir}/man8/bacula-fd.8*

%files sd
%defattr(644,root,root,755)
%doc LICENSE
%dir %{_sysconfdir}
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bacula-sd.conf
%attr(754,root,root) /etc/rc.d/init.d/bacula-sd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/bacula-sd
%attr(755,root,root) %{_sbindir}/bacula-sd
%attr(755,root,root) %{_sbindir}/bcopy
%attr(755,root,root) %{_sbindir}/bextract
%attr(755,root,root) %{_sbindir}/bls
%attr(755,root,root) %{_sbindir}/bscan
%attr(755,root,root) %{_sbindir}/btape
%attr(755,root,root) %{_libexecdir}/%{name}/mtx-changer
%attr(755,root,root) %{_libexecdir}/%{name}/disk-changer
%attr(755,root,root) %{_libexecdir}/%{name}/dvd-handler
%{_mandir}/man8/bacula-sd.8*
%{_mandir}/man8/bcopy.8*
%{_mandir}/man8/bextract.8*
%{_mandir}/man8/bls.8*
%{_mandir}/man8/bscan.8*
%{_mandir}/man8/btape.8*

%files console
%defattr(644,root,root,755)
%doc LICENSE
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bconsole.conf
%attr(755,root,root) %{_sbindir}/bconsole
%{_mandir}/man8/bconsole.8*

%if %{with console_wx}
%files console-wx
%defattr(644,root,root,755)
%doc LICENSE
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/bacula-wx.desktop
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bwx-console.conf
%attr(755,root,root) %{_sbindir}/bwx-console
%{_mandir}/man1/bacula-bwxconsole.1*
%endif

%if %{with gnome}
%files console-gnome
%defattr(644,root,root,755)
%doc LICENSE
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/bacula.desktop
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bgnome-console.conf
%attr(755,root,root) %{_sbindir}/bgnome-console
%{_mandir}/man1/bacula-bgnome-console.1*
%endif

%if %{with console_wx}
%files tray-monitor
%defattr(644,root,root,755)
%doc LICENSE
%{_pixmapsdir}/%{name}-tray-monitor.xpm
%{_desktopdir}/%{name}-tray-monitor.desktop
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tray-monitor.conf
%attr(755,root,root) %{_bindir}/bacula-tray-monitor
%{_mandir}/man1/bacula-tray-monitor.1*
%endif

%if %{with rescue}
%files rescue
%defattr(644,root,root,755)
%doc LICENSE
%dir %{_sysconfdir}/rescue
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rescue/backup.etc.list
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rescue/bacula-fd
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rescue/format_floppy
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rescue/getdiskinfo
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rescue/make_rescue_disk
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rescue/restore_bacula
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rescue/restore_etc
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rescue/run_grub
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rescue/run_lilo
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rescue/sfdisk.bz2
%endif
