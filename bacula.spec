## TODO:
#	- fix libtoolize
#	- update desktop files, think about su-wrappers for console (with .desktop files)
#	- fix log file permissions
#	- check on upgrade (5.0 and 5.2 databases are NOT compatible)
#
# Conditional build:
%if "%{pld_release}" == "ac"
%bcond_with	qt		# BAT / qt-console Qt4 GUI
%else
%bcond_without	qt		# BAT / qt-console Qt4 GUI
%endif
%bcond_without	mysql			# use MySQL
%bcond_without	pgsql			# use PostgreSQL
%bcond_without	sqlite3			# use SQLite3
%bcond_without	nagios		# build nagios plugin
%bcond_with	sqlite3_sync_off	# makes SQLite3 backend much faster, but less reliable

%if %{without sqlite3}
%undefine       with_sqlite3_sync_off
%endif

%define	qtver	4.8.4
Summary:	Bacula - The Network Backup Solution
Summary(pl.UTF-8):	Bacula - rozwiązanie do wykonywania kopii zapasowych po sieci
Name:		bacula
Version:	7.0.5
Release:	0.1
License:	AGPL v3
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/bacula/%{name}-%{version}.tar.gz
# Source0-md5:	b4a99d673f5e1eaae8b257ccc610241f
Source10:	%{name}-dir.init
Source11:	%{name}-fd.init
Source12:	%{name}-sd.init
Source13:	%{name}.logrotate
Source14:	%{name}-dir.sysconfig
Source15:	%{name}-fd.sysconfig
Source16:	%{name}-sd.sysconfig
Source17:	%{name}-dir.service
Source18:	%{name}-fd.service
Source19:	%{name}-sd.service
Patch0:		%{name}-mtx-changer.patch
Patch1:		%{name}-branding.patch
Patch2:		%{name}-desktop.patch
Patch3:		make_catalog_backup-setup-home.patch
Patch4:		%{name}-no_lockmgr.patch
URL:		http://www.bacula.org/
BuildRequires:	acl-devel
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libcap-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libwrap-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-modules
%if %{with qt}
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
%endif
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.644
BuildRequires:	sed >= 4.0
%{?with_sqlite3:BuildRequires:	sqlite3-devel}
BuildRequires:	which
Requires:	systemd-units >= 38
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/%{name}
%define		_localstatedir	/var/lib/%{name}
%define		nagiosplugindir	%{_libdir}/nagios/plugins

# db packages contain duplicates
%define		_duplicate_files_terminate_build	0

# from 'the worst' to 'the best'
%define	databases %{?with_sqlite3:sqlite3} %{?with_mysql:mysql} %{?with_pgsql:postgresql}

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
Conflicts:	logrotate < 3.8.0

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
Requires:	%{name}-common = %{version}-%{release}
Requires:	bacula(db) = %{version}-%{release}
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
record of all Volumes used, all Jobs run, and all Files saved.

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
plikami.

%package console
Summary:	Bacula Console
Summary(pl.UTF-8):	Konsola Baculi
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}

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

%package console-qt
Summary:	bat – The Bacula Administration Tool
Summary(pl.UTF-8):	bat – narzędzie administratora Baculi
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}
Requires:	QtCore >= %{qtver}
Obsoletes:	bacula-console-qt4 < 5.2.13-1

%description console-qt
Bacula - It comes by night and sucks the vital essence from your
computers.

bat is short for Bacula Administration Tool. It is a GUI form of
bconsole, but with many additional features.

%description console-qt -l pl.UTF-8
Bacula - przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

bat, czyli Bacula Administration Tool, jest graficznym odpowiednikiem
bconsole, z wieloma dodatkowymi funkcjami.

%package tray-monitor
Summary:	Bacula Tray Monitor
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}

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
Requires:	%{name}-common = %{version}-%{release}

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
Requires:	%{name}-common = %{version}-%{release}
Suggests:	mtx
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

%package db-postgresql
Summary:	PostgreSQL database driver for Bacula
Summary(pl.UTF-8):	Sterownik bazy PostgreSQL dla Baculi
Group:		Networking/Utilities
Requires(post):	/sbin/ldconfig
Requires:	%{name}-common = %{version}-%{release}
Provides:	bacula(db) = %{version}-%{release}
Obsoletes:	bacula(db)

%description db-postgresql
PostgreSQL database driver for Bacula.

%description db-postgresql -l pl.UTF-8
Sterownik bazy PostgreSQL dla Baculi.

%package db-mysql
Summary:	MySQL database driver for Bacula
Summary(pl.UTF-8):	Sterownik bazy MySQL dla Baculi
Group:		Networking/Utilities
Requires(post):	/sbin/ldconfig
Requires:	%{name}-common = %{version}-%{release}
Provides:	bacula(db) = %{version}-%{release}
Obsoletes:	bacula(db)

%description db-mysql
MySQL database driver for Bacula.

%description db-mysql -l pl.UTF-8
Sterownik bazy MySQL dla Baculi.

%package db-sqlite3
Summary:	SQLite database driver for Bacula
Summary(pl.UTF-8):	Sterownik bazy SQLite dla Baculi
Group:		Networking/Utilities
Requires(post):	/sbin/ldconfig
Requires:	%{name}-common = %{version}-%{release}
Provides:	bacula(db) = %{version}-%{release}
Obsoletes:	bacula(db)

%description db-sqlite3
SQLite database driver for Bacula.

%description db-sqlite3 -l pl.UTF-8
Sterownik bazy SQLite dla Baculi.

%package -n nagios-plugin-check_bacula
Summary:	Nagios plugin to check bacula
Group:		Networking
Requires:	nagios-common

%description -n nagios-plugin-check_bacula
Nagios plugin to check bacula.

%define	_noautoreq	libbaccats-%{version}.so
# provided by various db libraries as a symlink

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

sed -i -e 's#bindir=.*#bindir=%{_bindir}#g' \
	src/cats/create_* src/cats/delete_* src/cats/drop_* \
	src/cats/grant_* src/cats/make_* src/cats/update_*
sed -i -e 's/@hostname@/--hostname--/' src/*/*.conf.in
sed -i -e 's/@basename@/--hostname--/' src/*/*.conf.in

%build
cd autoconf
%{__aclocal} -I bacula-macros -I gettext-macros -I libtool
## $BUILD_DIR not seen by libtoolize, export it
#BUILD_DIR=.. %%{__libtoolize}
cd ..
%{__autoconf} --prepend-include=$(pwd)/autoconf autoconf/configure.in > configure

CPPFLAGS="-I/usr/include/ncurses -I%{_includedir}/readline"

QMAKE=%{_bindir}/qmake-qt4 \
%configure \
	DISTNAME=pld-linux \
	--with-scriptdir=%{_libexecdir}/%{name} \
	%{?with_qt:--enable-bat} \
	--disable-conio \
	--enable-smartalloc \
	--with-readline \
	--with-tcp-wrappers \
	--with-working-dir=%{_var}/lib/%{name} \
	--with-dump-email="root@localhost" \
	--with-job-email="root@localhost" \
	--with-smtp-host=localhost \
	--with-pid-dir=/var/run \
	--with-subsys-dir=/var/lock/subsys \
	--with-systemd=%{systemdunitdir} \
	--enable-batch-insert \
	%{?with_pgsql:--with-postgresql} \
	%{?with_mysql:--with-mysql} \
	%{?with_sqlite3:--with-sqlite3} \
	%{?with_sqlite3_sync_off:--enable-extra-sqlite3-init="pragma synchronous=0;"} \
	--with-dir-password="#FAKE-dir-password#" \
	--with-fd-password="#FAKE-fd-password#" \
	--with-sd-password="#FAKE-sd-password#" \
	--with-mon-dir-password="#FAKE-mon-dir-password#" \
	--with-mon-fd-password="#FAKE-mon-fd-password#" \
	--with-mon-sd-password="#FAKE-mon-sd-password#" \
	--with-openssl

%if %{with qt}
cd src/qt-console
qmake-qt4 bat.pro
cd ../..
%endif

%{__make} 2>&1 | tee log
# check for build errors
grep "Error in" log && exit 1

%if %{with nagios}
# nagios plugin
%{__make} -C examples/nagios/check_bacula
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,pam.d,sysconfig} \
		$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}} \
		$RPM_BUILD_ROOT{%{_mandir},%{_bindir},/var/log{,/archive}/bacula} \
		$RPM_BUILD_ROOT%{systemdunitdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# create copies of make_catalog_backup for specific databases; zeore default one (will be ghost)
for database in %{databases}; do
	sed -e "s#default_db_type=.*#default_db_type=${database}#g" \
		$RPM_BUILD_ROOT%{_libdir}/%{name}/make_catalog_backup \
		> $RPM_BUILD_ROOT%{_libdir}/%{name}/make_${database}_catalog_backup
		chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/make_${database}_catalog_backup
done
:> $RPM_BUILD_ROOT%{_libdir}/%{name}/make_catalog_backup

# we use db dependant (at compile time) shell script only
rm $RPM_BUILD_ROOT%{_libexecdir}/%{name}/make_catalog_backup.pl

## replace with empty file, replaced by ldconfig from each db-* package on intsall
rm $RPM_BUILD_ROOT%{_libdir}/libbaccats-%{version}.so
touch $RPM_BUILD_ROOT%{_libdir}/libbaccats-%{version}.so

install -p %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-dir
install -p %{SOURCE11} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-fd
install -p %{SOURCE12} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-sd
cp -a %{SOURCE13} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}-dir
cp -a %{SOURCE14} $RPM_BUILD_ROOT/etc/sysconfig/bacula-dir
cp -a %{SOURCE15} $RPM_BUILD_ROOT/etc/sysconfig/bacula-fd
cp -a %{SOURCE16} $RPM_BUILD_ROOT/etc/sysconfig/bacula-sd
cp -a %{SOURCE17} $RPM_BUILD_ROOT%{systemdunitdir}/bacula-dir.service
cp -a %{SOURCE18} $RPM_BUILD_ROOT%{systemdunitdir}/bacula-fd.service
cp -a %{SOURCE19} $RPM_BUILD_ROOT%{systemdunitdir}/bacula-sd.service

%if %{with qt}
# qmake somewhy does not always create install_bins target. install our own the bin
rm -f $RPM_BUILD_ROOT%{_sbindir}/bat
libtool --silent --mode=install install src/qt-console/bat $RPM_BUILD_ROOT%{_bindir}
cp -a scripts/bacula.png $RPM_BUILD_ROOT%{_pixmapsdir}/bacula.png
cp -a scripts/bat.desktop $RPM_BUILD_ROOT%{_desktopdir}
%endif

touch $RPM_BUILD_ROOT/var/log/bacula/log

# install the updatedb scripts for older versions that last full release
# 2.0 -> 3.0 : 10_to_11
# 5.0 -> 5.2 : 12_to_14
install -p updatedb/update_*_tables_10_to_11 $RPM_BUILD_ROOT%{_libexecdir}/%{name}
install -p updatedb/update_*_tables_11_to_12 $RPM_BUILD_ROOT%{_libexecdir}/%{name}
install -p updatedb/update_*_tables_12_to_14 $RPM_BUILD_ROOT%{_libexecdir}/%{name}

# place for site passwords
touch $RPM_BUILD_ROOT%{_sysconfdir}/{dir-password,fd-password,sd-password}
touch $RPM_BUILD_ROOT%{_sysconfdir}/{mon-dir-password,mon-fd-password,mon-sd-password}

mv $RPM_BUILD_ROOT%{_libexecdir}/%{name}/mtx-changer.conf $RPM_BUILD_ROOT%{_sysconfdir}/mtx-changer.conf

# some file changes
rm -f $RPM_BUILD_ROOT%{_libexecdir}/%{name}/{gconsole,startmysql,stopmysql,bacula,bconsole,fd}

rm $RPM_BUILD_ROOT%{_docdir}/bacula/ChangeLog
rm $RPM_BUILD_ROOT%{_docdir}/bacula/INSTALL
rm $RPM_BUILD_ROOT%{_docdir}/bacula/LICENSE
rm $RPM_BUILD_ROOT%{_docdir}/bacula/README
rm $RPM_BUILD_ROOT%{_docdir}/bacula/ReleaseNotes
rm $RPM_BUILD_ROOT%{_docdir}/bacula/VERIFYING
rm $RPM_BUILD_ROOT%{_docdir}/bacula/technotes

# startup scripts, those in /etc/rc.d/init.d are better
rm $RPM_BUILD_ROOT%{_sbindir}/bacula
rm $RPM_BUILD_ROOT%{_libexecdir}/%{name}/bacula-ctl-*

# unsupported
rm $RPM_BUILD_ROOT%{_libexecdir}/%{name}/btraceback.mdb

# rename to avoid possible conflicts
mv $RPM_BUILD_ROOT%{_sbindir}/{,bacula-}dbcheck
mv $RPM_BUILD_ROOT%{_mandir}/man8/{,bacula-}dbcheck.8.gz

# no -devel files packaged, so this is also useless
rm $RPM_BUILD_ROOT%{_libdir}/libbac{,cfg,find,sql,cats}.{so,la}
#rm $RPM_BUILD_ROOT%{_libdir}/libbaccats*.{so,la}
%{?with_mysql:rm $RPM_BUILD_ROOT%{_libdir}/libbaccats-mysql.{la,so}}
%{?with_pgsql:rm $RPM_BUILD_ROOT%{_libdir}/libbaccats-postgresql.{la,so}}
%{?with_sqlite3:rm $RPM_BUILD_ROOT%{_libdir}/libbaccats-sqlite3.{la,so}}

%if %{with nagios}
install -d $RPM_BUILD_ROOT%{nagiosplugindir}
%{__make} -C examples/nagios/check_bacula install \
	sbindir=%{nagiosplugindir} \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre common
%groupadd -P %{name}-common -g 136 -r -f bacula
%useradd -P %{name}-common -u 136 -r -d /var/lib/bacula -s /bin/false -c "Bacula User" -g bacula bacula

%define update_configs \
echo "Updating bacula passwords and names..." | %banner -a %{name} \
cd %{_sysconfdir} \
for f in *-password; do \
	if [ ! -s $f ]; then \
		openssl rand -base64 33 > $f \
	fi \
	p=$(cat $f) \
	for cf in *.conf *.conf.rpmnew; do \
		[ -f $cf ] && sed -i -e"s:#FAKE-$f#:$p:" "$cf" || : \
	done \
done \
for cf in *.conf *.conf.rpmnew; do \
	[ -f $cf ] && sed -i -e"s:--hostname--:`hostname`:" "$cf" || : \
done

%post common
/sbin/ldconfig
%update_configs

%postun common
/sbin/ldconfig
if [ "$1" = "0" ]; then
	%userremove bacula
	%groupremove bacula
fi

%triggerpostun dir -- %{name}-dir < %{version}-0
%banner bacula-dir -t3 <<EOF
You have upgraded from an older version of Bacula director.

You will probably need to call %{_libexecdir}/%{name}/update_bacula_tables
script to upgrade the database.

Ensure you database partition has enough free space before you run the upgrade,
i.e check that there is enough room to rebuild 'File' table (it is the largest
in bacula db).

EOF

%post dir
%update_configs
/sbin/chkconfig --add bacula-dir
%service bacula-dir restart "Bacula Director daemon"
%systemd_post bacula-dir.service

%preun dir
if [ "$1" = "0" ]; then
	%service bacula-dir stop
	/sbin/chkconfig --del bacula-dir
fi
%systemd_preun bacula-dir.service

%postun dir
%systemd_reload

%post fd
%update_configs
/sbin/chkconfig --add bacula-fd
%service bacula-fd restart "Bacula File daemon"
%systemd_post bacula-fd.service

%preun fd
if [ "$1" = "0" ]; then
	%service bacula-fd stop
	/sbin/chkconfig --del bacula-fd
fi
%systemd_preun bacula-fd.service

%postun fd
%systemd_reload

%post sd
%update_configs
/sbin/chkconfig --add bacula-sd
%service bacula-sd restart "Bacula Storage daemon"
%systemd_post bacula-sd.service

%preun sd
if [ "$1" = "0" ]; then
	%service bacula-sd stop
	/sbin/chkconfig --del bacula-sd
fi
%systemd_preun bacula-sd.service

%postun sd
%systemd_reload

%pre console
if [ -e %{_sysconfdir}/console.conf -a ! -e %{_sysconfdir}/bconsole.conf ]; then
	mv %{_sysconfdir}/console.conf %{_sysconfdir}/bconsole.conf
fi

%post console
%update_configs

%triggerpostun common -- %{name}-common < 5.0.1-2
find %{_sysconfdir}/bat.conf* -perm /007 -print0 2>/dev/null | xargs -0 -r chmod 600 || :

%post console-qt
%update_configs

%post tray-monitor
%update_configs

%define db_post() \
/sbin/ldconfig \
for name in "create database" "drop tables" "drop database" "grant privileges" "make tables" "update tables"; do \
	prefix="${name%% *}" \
	suffix="${name#* }" \
	ln -sf "${prefix}_%{1}_${suffix}" %{_libexecdir}/%{name}/"${prefix}_bacula_${suffix}" || : \
done \
ln -sf "make_%{1}_catalog_backup" %{_libexecdir}/%{name}/make_catalog_backup || : \
ln -sf libbaccats-%{1}-%{version}.so %{_libdir}/libbaccats-%{version}.so || : \
%service bacula-dir restart "Bacula Director daemon"

%post db-postgresql
%db_post postgresql

%postun db-postgresql -p /sbin/ldconfig

%post db-mysql
%db_post mysql

%postun db-mysql -p /sbin/ldconfig

%post db-sqlite3
%db_post sqlite3

%postun db-sqlite3 -p /sbin/ldconfig

%files common
%defattr(644,root,root,755)
%doc LICENSE
%dir %{_sysconfdir}
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*-password
# do not remove bsmtp from files. Fix build if it is not installed.
%attr(755,root,root) %{_sbindir}/bpluginfo
%attr(755,root,root) %{_sbindir}/bsmtp
%attr(755,root,root) %{_sbindir}/btraceback
%attr(755,root,root) %{_libdir}/libbac-7*.so
%attr(755,root,root) %{_libdir}/libbaccfg-7*.so
%attr(755,root,root) %{_libdir}/libbacfind-7*.so
%attr(755,root,root) %{_libdir}/libbacsql-7*.so
%{_mandir}/man8/bacula.8*
%{_mandir}/man8/bpluginfo.8*
%{_mandir}/man1/bsmtp.1*
%{_mandir}/man8/btraceback.8*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/btraceback.dbx
%{_libexecdir}/%{name}/btraceback.gdb
%{_libexecdir}/%{name}/bacula_config
%attr(770,root,bacula) %dir %{_localstatedir}
%attr(750,bacula,logs) %dir /var/log/bacula
%attr(640,bacula,logs) %ghost /var/log/bacula/log
%attr(750,bacula,logs) %dir /var/log/archive/bacula

%files dir
%defattr(644,root,root,755)
%doc ChangeLog ReleaseNotes LICENSE
#%doc examples %{name}-docs-%{version}/manual/{*.pdf,bacula}
%attr(640,root,bacula) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bacula-dir.conf
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/bacula-dir
%attr(754,root,root) /etc/rc.d/init.d/bacula-dir
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/bacula-dir
%{systemdunitdir}/bacula-dir.service
%attr(755,root,root) %{_sbindir}/bacula-dir
%attr(755,root,root) %{_sbindir}/bregex
%attr(755,root,root) %{_sbindir}/bwild
%attr(755,root,root) %{_sbindir}/bacula-dbcheck
%{_mandir}/man8/bacula-dir.8*
%{_mandir}/man8/bacula-dbcheck.8*
%{_mandir}/man8/bregex.8*
%{_mandir}/man8/bwild.8*
%{_libexecdir}/%{name}/query.sql
%attr(755,root,root) %{_libexecdir}/%{name}/delete_catalog_backup

%if %{with pgsql}
%files db-postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/%{name}/create_postgresql_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_postgresql_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_postgresql_tables
%attr(755,root,root) %{_libexecdir}/%{name}/grant_postgresql_privileges
%attr(755,root,root) %{_libexecdir}/%{name}/make_postgresql_tables
%attr(755,root,root) %{_libexecdir}/%{name}/update_postgresql_*
%attr(755,root,root) %{_libexecdir}/%{name}/make_postgresql_catalog_backup
%attr(755,root,root) %{_libdir}/libbaccats-postgresql-7*.so

%ghost %attr(755,root,root) %{_libdir}/libbaccats-7*.so
%ghost %{_libexecdir}/%{name}/create_bacula_database
%ghost %{_libexecdir}/%{name}/drop_bacula_tables
%ghost %{_libexecdir}/%{name}/drop_bacula_database
%ghost %{_libexecdir}/%{name}/grant_bacula_privileges
%ghost %{_libexecdir}/%{name}/make_bacula_tables
%ghost %{_libexecdir}/%{name}/update_bacula_tables
%ghost %{_libexecdir}/%{name}/make_catalog_backup
%endif

%if %{with mysql}
%files db-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/%{name}/create_mysql_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_mysql_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_mysql_tables
%attr(755,root,root) %{_libexecdir}/%{name}/grant_mysql_privileges
%attr(755,root,root) %{_libexecdir}/%{name}/make_mysql_tables
%attr(755,root,root) %{_libexecdir}/%{name}/update_mysql_*
%attr(755,root,root) %{_libexecdir}/%{name}/make_mysql_catalog_backup
%attr(755,root,root) %{_libdir}/libbaccats-mysql-7*.so

%ghost %attr(755,root,root) %{_libdir}/libbaccats-7*.so
%ghost %{_libexecdir}/%{name}/create_bacula_database
%ghost %{_libexecdir}/%{name}/drop_bacula_tables
%ghost %{_libexecdir}/%{name}/drop_bacula_database
%ghost %{_libexecdir}/%{name}/grant_bacula_privileges
%ghost %{_libexecdir}/%{name}/make_bacula_tables
%ghost %{_libexecdir}/%{name}/update_bacula_tables
%ghost %{_libexecdir}/%{name}/make_catalog_backup
%endif

%if %{with sqlite3}
%files db-sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/%{name}/create_sqlite3_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_sqlite3_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_sqlite3_tables
%attr(755,root,root) %{_libexecdir}/%{name}/grant_sqlite3_privileges
%attr(755,root,root) %{_libexecdir}/%{name}/make_sqlite3_tables
%attr(755,root,root) %{_libexecdir}/%{name}/update_sqlite3_*
%attr(755,root,root) %{_libexecdir}/%{name}/make_sqlite3_catalog_backup
%attr(755,root,root) %{_libdir}/libbaccats-sqlite3-7*.so

%ghost %attr(755,root,root) %{_libdir}/libbaccats-7*.so
%ghost %{_libexecdir}/%{name}/create_bacula_database
%ghost %{_libexecdir}/%{name}/drop_bacula_tables
%ghost %{_libexecdir}/%{name}/drop_bacula_database
%ghost %{_libexecdir}/%{name}/grant_bacula_privileges
%ghost %{_libexecdir}/%{name}/make_bacula_tables
%ghost %{_libexecdir}/%{name}/update_bacula_tables
%ghost %{_libexecdir}/%{name}/make_catalog_backup
%endif

%files fd
%defattr(644,root,root,755)
%doc LICENSE
%attr(640,root,bacula) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bacula-fd.conf
%attr(754,root,root) /etc/rc.d/init.d/bacula-fd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/bacula-fd
%{systemdunitdir}/bacula-fd.service
%attr(755,root,root) %{_sbindir}/bacula-fd
%attr(755,root,root) %{_libdir}/bpipe-fd.so
%{_mandir}/man8/bacula-fd.8*

%files sd
%defattr(644,root,root,755)
%doc LICENSE
%attr(640,root,bacula) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bacula-sd.conf
%attr(640,root,bacula) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mtx-changer.conf
%attr(754,root,root) /etc/rc.d/init.d/bacula-sd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/bacula-sd
%{systemdunitdir}/bacula-sd.service
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
%attr(640,root,bacula) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bconsole.conf
%attr(755,root,root) %{_sbindir}/bconsole
%{_mandir}/man8/bconsole.8*

%if %{with qt}
%files console-qt
%defattr(644,root,root,755)
%doc LICENSE
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/bat.desktop
# Do not make this file world-readable or any user will get full access to the
# backup system
%attr(640,root,bacula) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bat.conf
%attr(755,root,root) %{_bindir}/bat
%{_mandir}/man1/bat.1*
%{_docdir}/%{name}
%endif

%if %{with nagios}
%files -n nagios-plugin-check_bacula
%defattr(644,root,root,755)
%attr(755,root,root) %{nagiosplugindir}/check_bacula
%endif
