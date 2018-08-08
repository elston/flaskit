#!/bin/bash
# ..
oldfile='/docker-entrypoint-initdb.d/bootstrap.sql.template'
newfile='/docker-entrypoint-initdb.d/bootstrap.sql'
# ..
cp ${oldfile} ${newfile}
sed -i -r 's/DB_NAME/'${DB_NAME}'/g' ${newfile}
sed -i -r 's/DB_USER/'${DB_USER}'/g' ${newfile}
sed -i -r 's/DB_PASSWORD/'${DB_PASSWORD}'/g' ${newfile}

# ..
/usr/local/bin/docker-entrypoint.sh postgres
