#!/bin/bash

INSERT_DATA=true
RECREATE=false

COLOR="\x1B[93m"
NO_COLOR="\x1B[0m"

while test $# -gt 0; do
  case "$1" in
    -h|--help)
      echo -e "${COLOR}create_test_db - Create a test SQLite Database${NO_COLOR}"
      echo " "
      echo "create_test_db [arguments]"
      echo " "
      echo "options:"
      echo "-h, --help                Show brief help"
      echo "--skip-data               Skip the insertion of test data into the database"
      echo "--recreate                Remove the existing database if present"
      exit 0
    ;;
    --skip-data)
      INSERT_DATA=false
      shift
    ;;
    --recreate)
      RECREATE=true
      shift
    ;;
    *)
      break
    ;;
  esac
done

DB_FILE="$PWD/gadget.db"

if [ -f $DB_FILE ]; then
  if [ "$RECREATE" = true ]; then
    echo -e "${COLOR}Removing exisiting database $DB_FILE${NO_COLOR}"
    rm -f $DB_FILE
  else
    echo -e "${COLOR}$DB_FILE already exists!${NO_COLOR}"
    exit 1
  fi
fi

# Create the DB
echo -e "${COLOR}Creating database: $DB_FILE${NO_COLOR}"
touch $DB_FILE

# Run migrations
echo -e "${COLOR}Running migrations${NO_COLOR}"
alembic upgrade head

# Insert testing data
if [ "$INSERT_DATA"=true ]; then
  echo -e "${COLOR}Inserting test data${NO_COLOR}"
  python $PWD/testdata.py
fi

echo -e "${COLOR}Finished${NO_COLOR}"
