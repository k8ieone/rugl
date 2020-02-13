package org.learning.api;

import org.learning.model.HabitableBuilding;
import org.learning.model.HabitableBuildingException;
import org.learning.model.HabitableBuildingTypes;

import javax.sql.DataSource;
import java.sql.Array;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public interface HabitableBuildingsManager {

    public void addToDB(Habitable building) throws HabitableBuildingException;
    public void deleteFromDB(Habitable building) throws HabitableBuildingException;
    public HabitableBuilding SetToHabitableBuilding(ResultSet resultSet) throws SQLException;
    public HabitableBuilding selectFromDBbyLocation(Array location) throws HabitableBuildingException;
    public ArrayList<HabitableBuilding> selectFromDBbyType(HabitableBuildingTypes type) throws HabitableBuildingException;
}
