# TODO:
# - install section
# - build section
# - files section
# - pld configs and init scripts
#
Summary:	Bacula - The Network Backup Solution
Name:		bacula
Version:	1.34.6
Release:	0.1
Group:		Networking/Utilities
License:	GPL v2
Source0:	http://dl.sourceforge.net/bacula/%{name}-%{version}.tar.gz
# Source0-md5:	c8aaef1429f9b37efce381f49f7bccb8
Source1:	http://www.tux.org/pub/distributions/tinylinux/tomsrtbt/tomsrtbt-2.0.103.tar.gz
# Source1-md5:	d5ee50efb28986d564547d5da5de2483
URL:		http://www.bacula.org/
BuildRequires:	wxGTK2-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	sqlite2-devel
BuildRequires:	libwrap-devel
BuildRequires:	zlib-devel
BuildRequires:	acl-devel
BuildRequires:	libstdc++-devel
Provides:	bacula-dir
Provides:	bacula-sd
Provides:	bacula-fd
Provides:	bacula-server
Conflicts:	bacula-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

%package client
Summary:	Bacula - The Network Backup Solution
Group:		Networking/Utilities
Provides:	bacula-fd

%description client
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

This is the File daemon (Client) only package. It includes the command
line console program.

%package rescue

Summary:	Bacula - The Network Backup Solution
Group:		Networking/Utilities
Requires:	coreutils
Requires:	util-linux
Requires:	libc5
Requires:	bacula-fd

%description rescue
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

This package installs scripts for disaster recovery and builds rescue
floppy disks for bare metal recovery. This package includes tomsrtbt
(http://www.toms.net/rb/, by Tom Oehser, Tom@Toms.NET) to provide a
tool to build a boot floppy disk.

You need to have the bacula-sqlite, bacula-mysql, bacula-postgresql or
bacula-client package for your platform installed and configured
before installing this package.

To create a boot disk run "./getdiskinfo" from the /etc/bacula/rescue
directory (this is done when the package is first installed), then run
"./install.s" from the /etc/bacula/rescue/tomsrtbt/ directory. To make
the bacula rescue disk run "./make_rescue_disk --copy-static-bacula
- --copy-etc-files" from the /etc/bacula/rescue directory. To recreate
  the rescue information for this system run ./getdiskinfo again.

%package updatedb
Summary:	Bacula - The Network Backup Solution
Group:		Networking/Utilities

%description updatedb
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

This package installs scripts for updating older versions of the
bacula database.

%package wxconsole
Summary:	Bacula - The Network Backup Solution
Group:		Networking/Utilities
Requires:	bacula-fd

%description wxconsole
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

This is the WX Console package. It is an add-on to the client or
server packages.

%prep
%setup -q -b 1
sed -i -e 's#wx-config#wxgtk2-2.4-config#g' configure*
sed -i -e 's#-lreadline -ltermcap#-lreadline#g' configure*

%build
# patches for the bundled sqlite scripts
# patch the make_sqlite_tables script for installation bindir
patch src/cats/make_sqlite_tables.in src/cats/make_sqlite_tables.in.patch
# patch the create_sqlite_database script for installation bindir
patch src/cats/create_sqlite_database.in src/cats/create_sqlite_database.in.patch
# patch the make_catalog_backup script for installation bindir
patch src/cats/make_catalog_backup.in src/cats/make_catalog_backup.in.patch
# patch the update_sqlite_tables script for installation bindir
patch src/cats/update_sqlite_tables.in src/cats/update_sqlite_tables.in.patch

CPPFLAGS="-I%{_includedir}/ncurses -I%{_includedir}/readline"
%configure \
	--disable-gnome \
	--disable-conio \
	--enable-wx-console \
	--with-readline \
	--with-tcp-wrappers \
	--with-working-dir=%{_var}/lib/%{name} \
	--with-dump-email="root@localhost" \
	--with-job-email="root@localhost" \
	--with-smtp-host=localhost \
	--with-pid-dir=/var/run \
	--with-subsys-dir=/var/lock/subsys \
	--with-sqlite
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/init.d
install -d $RPM_BUILD_ROOT/etc/logrotate.d
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -d $RPM_BUILD_ROOT%{_datadir}/applications
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/tomsrtbt
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bacula/updatedb
install -d $RPM_BUILD_ROOT/etc/pam.d
install -d $RPM_BUILD_ROOT/etc/security/console.apps
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# setup the manual for the doc dir and correct some broken CVS permissions
mkdir html-manual
cp -p doc/html-manual/*.html html-manual/
cp -p doc/html-manual/*.jpg html-manual/
cp -p doc/html-manual/*.gif html-manual/
cp -p doc/html-manual/*.css html-manual/

cp -p platforms/redhat/bacula-dir $RPM_BUILD_ROOT%{_sysconfdir}/init.d/bacula-dir
cp -p platforms/redhat/bacula-fd $RPM_BUILD_ROOT%{_sysconfdir}/init.d/bacula-fd
cp -p platforms/redhat/bacula-sd $RPM_BUILD_ROOT%{_sysconfdir}/init.d/bacula-sd
chmod 0754 $RPM_BUILD_ROOT%{_sysconfdir}/init.d/*

cp -p scripts/bacula.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/bacula.png
cp -p scripts/bacula.desktop.gnome2.consolehelper $RPM_BUILD_ROOT%{_datadir}/applications/bacula.desktop
cp -p scripts/gnome-console.console_apps $RPM_BUILD_ROOT/etc/security/console.apps/gnome-console
cp -p scripts/gnome-console.pamd $RPM_BUILD_ROOT/etc/pam.d/gnome-console
ln -sf consolehelper $RPM_BUILD_ROOT%{_bindir}/gnome-console

cp -p ../depkgs/sqlite/sqlite $RPM_BUILD_ROOT%{sqlite_bindir}/sqlite
cp -p ../depkgs/sqlite/sqlite.h $RPM_BUILD_ROOT%{sqlite_bindir}/sqlite.h
cp -p ../depkgs/sqlite/libsqlite.a $RPM_BUILD_ROOT%{sqlite_bindir}/libsqlite.a

# install the logrotate file
cp -p scripts/logrotate $RPM_BUILD_ROOT/etc/logrotate.d/bacula

# install the rescue stuff
# these are the rescue scripts
cp -p rescue/linux/backup.etc.list $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/
cp -p rescue/linux/format_floppy $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/
cp -p rescue/linux/getdiskinfo $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/
cp -p rescue/linux/make_rescue_disk $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/
cp -p rescue/linux/restore_bacula $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/
cp -p rescue/linux/restore_etc $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/
cp -p rescue/linux/run_grub $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/
cp -p rescue/linux/run_lilo $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/
cp -p rescue/linux/sfdisk.bz2 $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/

# this is the static file daemon
cp -p src/filed/static-bacula-fd $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/bacula-fd

# this is the tom's root boot disk
cp -p ../%{tomsrtbt}/* $RPM_BUILD_ROOT%{_sysconfdir}/bacula/rescue/tomsrtbt/

# install the updatedb scripts
cp -p updatedb/* $RPM_BUILD_ROOT%{_sysconfdir}/bacula/updatedb/

# now clean up permissions that are left broken by the install
chmod o-r $RPM_BUILD_ROOT%{_sysconfdir}/bacula/query.sql
chmod o-rwx $RPM_BUILD_ROOT/var/bacula

%pre sqlite
# test for bacula database older than version 6
if [ -s %{_var}/lib/%{name}/bacula.db ];then
	DB_VER=`echo "select * from Version;" | %{sqlite_bindir}/sqlite %{_var}/lib/%{name}/bacula.db | tail -n 1 2>/dev/null`
	if [ -n "$DB_VER" ] && [ "$DB_VER" -lt "6" ]; then
		echo "This bacula upgrade will update a bacula database from version 6 to 7."
		echo "You appear to be running database version $DB_VER. You must first update"
		echo "your database to version 6 and then install this upgrade. The alternative"
		echo "is to use /etc/bacula/drop_sqlite_tables to delete all your your current"
		echo "catalog information, then do the upgrade. Information on updating a"
		echo "database older than version 6 can be found in the release notes."
		exit 1
	fi
fi
# check for and copy /etc/bacula/console.conf to bconsole.conf
if [ -s /etc/bacula/console.conf ];then
	cp -p /etc/bacula/console.conf /etc/bacula/bconsole.conf
fi

%post sqlite
# add our links
if [ "$1" -ge 1 ] ; then
	/sbin/chkconfig --add bacula-dir
	/sbin/chkconfig --add bacula-fd
	/sbin/chkconfig --add bacula-sd
fi

# test for an existing database
if [ -s %{_var}/lib/%{name}/bacula.db ]; then
	DB_VER=`echo "select * from Version;" | %{sqlite_bindir}/sqlite %{_var}/lib/%{name}/bacula.db | tail -n 1 2>/dev/null`
	# check to see if we need to upgrade a 1.32 or lower database
	if [ "$DB_VER" -lt "7" ]; then
		echo "This release requires an upgrade to your bacula database."
		echo "Backing up your current database..."
		echo ".dump" | %{sqlite_bindir}/sqlite %{_var}/lib/%{name}/bacula.db | bzip2 > %{_var}/lib/%{name}/bacula_backup.sql.bz2
		echo "Upgrading bacula database ..."
		/etc/bacula/update_sqlite_tables
		echo "If bacula works correctly you can remove the backup file %{_var}/lib/%{name}/bacula_backup.sql.bz2"
	fi
else
	# create the database and tables
	echo "Hmm, doesn't look like you have an existing database."
	echo "Creating SQLite database..."
	/etc/bacula/create_sqlite_database
	echo "Creating the SQLite tables..."
	/etc/bacula/make_sqlite_tables
fi

%preun sqlite
# delete our links
if [ $1 = 0 ]; then
	/sbin/chkconfig --del bacula-dir
	/sbin/chkconfig --del bacula-fd
	/sbin/chkconfig --del bacula-sd
fi

%post client
# add our link
if [ "$1" -ge 1 ] ; then
	/sbin/chkconfig --add bacula-fd
fi

%preun client
# delete our link
if [ $1 = 0 ]; then
	/sbin/chkconfig --del bacula-fd
fi

%post updatedb
echo "The database update scripts were installed to /etc/bacula/updatedb"

%clean
rm -rf $RPM_BUILD_ROOT

%post rescue
# link our current installed conf file to the rescue directory
ln -s /etc/bacula-fd.conf /etc/bacula/rescue/bacula-fd.conf

# run getdiskinfo
echo "Creating rescue files for this system..."
cd /etc/bacula/rescue
./getdiskinfo

%preun rescue
# remove the files created after the initial rpm installation
rm -f /etc/bacula/rescue/bacula-fd.conf
rm -f /etc/bacula/rescue/partition.*
rm -f /etc/bacula/rescue/format.*
rm -f /etc/bacula/rescue/mount_drives
rm -f /etc/bacula/rescue/start_network
rm -f /etc/bacula/rescue/sfdisk
rm -rf /etc/bacula/rescue/diskinfo/*

%files
%defattr(644,root,root,755)
%{_sysconfdir}/bacula/bacula
%{_sysconfdir}/bacula/bconsole
%{_sysconfdir}/bacula/fd
%{_sysconfdir}/bacula/create_bacula_database
%{_sysconfdir}/bacula/drop_bacula_database
%{_sysconfdir}/bacula/grant_bacula_privileges
%{_sysconfdir}/bacula/make_bacula_tables
%{_sysconfdir}/bacula/drop_bacula_tables
%{_sysconfdir}/bacula/update_bacula_tables
%{_sysconfdir}/bacula/create_sqlite_database
%{_sysconfdir}/bacula/drop_sqlite_database
%{_sysconfdir}/bacula/grant_sqlite_privileges
%{_sysconfdir}/bacula/make_sqlite_tables
%{_sysconfdir}/bacula/drop_sqlite_tables
%{_sysconfdir}/bacula/update_sqlite_tables
%{_sysconfdir}/bacula/make_catalog_backup
%{_sysconfdir}/bacula/delete_catalog_backup
%{_sysconfdir}/bacula/mtx-changer
%{_sysconfdir}/init.d/bacula-dir
%{_sysconfdir}/init.d/bacula-fd
%{_sysconfdir}/init.d/bacula-sd

%doc COPYING ChangeLog ReleaseNotes VERIFYING kernstodo doc/bacula.pdf html-manual
%{_mandir}/man1/*

/etc/logrotate.d/bacula

%config(noreplace) %{_sysconfdir}/bacula/bacula-dir.conf
%config(noreplace) %{_sysconfdir}/bacula/bacula-fd.conf
%config(noreplace) %{_sysconfdir}/bacula/bacula-sd.conf
%config(noreplace) %{_sysconfdir}/bacula/bconsole.conf
%{_sysconfdir}/bacula/query.sql
%{sqlite_bindir}/libsqlite.a
%{sqlite_bindir}/sqlite.h
%dir %{_var}/lib/%{name}

%attr(755,root,root) %{_sbindir}/bacula-dir
%attr(755,root,root) %{_sbindir}/bacula-fd
%attr(755,root,root) %{_sbindir}/bacula-sd
%attr(755,root,root) %{_sbindir}/bcopy
%attr(755,root,root) %{_sbindir}/bextract
%attr(755,root,root) %{_sbindir}/bls
%attr(755,root,root) %{_sbindir}/bscan
%attr(755,root,root) %{_sbindir}/btape
%attr(755,root,root) %{_sbindir}/btraceback
%attr(755,root,root) %{_sbindir}/bconsole
%attr(755,root,root) %{_sbindir}/dbcheck
%attr(755,root,root) %{_sbindir}/loaderinfo
%attr(755,root,root) %{_sbindir}/mtx
%attr(755,root,root) %{_sbindir}/scsitape
%attr(755,root,root) %{_sbindir}/bsmtp
%attr(755,root,root) %{_sbindir}/tapeinfo
%attr(755,root,root) %{_sbindir}/static-bacula-fd
%{sqlite_bindir}/sqlite
%{_sysconfdir}/bacula/btraceback.gdb

%files client
%defattr(644,root,root,755)

%{_sysconfdir}/bacula/fd
%{_sysconfdir}/bacula/bconsole
%{_sysconfdir}/init.d/bacula-fd

%doc COPYING ChangeLog ReleaseNotes VERIFYING kernstodo doc/bacula.pdf html-manual ../Release_Notes-%{version}-%{release}.txt
/etc/logrotate.d/bacula

%config(noreplace) %{_sysconfdir}/bacula/bacula-fd.conf
%config(noreplace) %{_sysconfdir}/bacula/bconsole.conf
%dir %{_var}/lib/%{name}

%attr(755,root,root) %{_sbindir}/bacula-fd
%attr(755,root,root) %{_sbindir}/btraceback
%{_sysconfdir}/bacula/btraceback.gdb
%attr(755,root,root) %{_sbindir}/bsmtp
%attr(755,root,root) %{_sbindir}/bconsole

%files rescue
%defattr(644,root,root,755)
%{_sysconfdir}/bacula/rescue/backup.etc.list
%{_sysconfdir}/bacula/rescue/format_floppy
%{_sysconfdir}/bacula/rescue/getdiskinfo
%{_sysconfdir}/bacula/rescue/make_rescue_disk
%{_sysconfdir}/bacula/rescue/restore_bacula
%{_sysconfdir}/bacula/rescue/restore_etc
%{_sysconfdir}/bacula/rescue/run_grub
%{_sysconfdir}/bacula/rescue/run_lilo
%{_sysconfdir}/bacula/rescue/sfdisk.bz2
%{_sysconfdir}/bacula/rescue/bacula-fd
%{_sysconfdir}/bacula/rescue/tomsrtbt/*

%files updatedb
%defattr(644,root,root,755)
%{_sysconfdir}/bacula/updatedb/*

%files wxconsole
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/wx-console
%{_sysconfdir}/bacula/wxconsole
%config(noreplace) %{_sysconfdir}/bacula/gnome-console.conf
%{_datadir}/pixmaps/bacula.png
%{_datadir}/applications/bacula.desktop

# add the console helper files
%config(noreplace,missingok) /etc/pam.d/gnome-console
%config(noreplace,missingok) /etc/security/console.apps/gnome-console
