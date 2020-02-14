package org.learning.managers;

import org.learning.api.Habitable;
import org.learning.model.HabitableBuilding;
import org.learning.model.HabitableBuildingException;
import org.learning.model.HabitableBuildingTypes;

import javax.sql.DataSource;
import java.sql.*;
import java.util.ArrayList;

public class HabitableBuildingsManagerImplementation implements org.learning.api.HabitableBuildingsManager {

    private DataSource dataSource;

    public HabitableBuildingsManagerImplementation(DataSource dataSource){
        this.dataSource = dataSource;
    }

    @Override
    public void addToDB(Habitable building) throws HabitableBuildingException {

        try (Connection connection = dataSource.getConnection()){
            try (PreparedStatement statement = connection.prepareStatement("INSERT INTO HabitableBuildings (MaxInhabitants, CurrentInhabitants, Size, Coordinates, Type, Active) VALUES ?, ?, ?, ?, ?, ?")){
                statement.    setInt(1, building.getMaxInhabitants());
                statement.    setInt(2, building.getCurrentInhabitants());
                statement.    setInt(3, building.getSize());
                statement. setString(4, building.getCoordinates());
                statement. setObject(5, building.getType());
                statement.setBoolean(6, building.getBuildingsState());

                statement.executeUpdate();

            } catch (SQLException e) {
                throw new HabitableBuildingException("Problem with connection", e);
            }

        } catch (SQLException e) {
            throw new HabitableBuildingException("Problem with connection", e);
        }
    }

    @Override
    public void deleteFromDB(Habitable building) throws HabitableBuildingException {

        try (Connection connection = dataSource.getConnection()){
            try (PreparedStatement statement = connection.prepareStatement("DELETE FROM HabitableBuildings WHERE Coordinates = ?")) {
                statement.setString(1, building.getCoordinates());
                statement.executeUpdate();

            } catch (SQLException e) {
                throw new HabitableBuildingException("Problem with connection", e);
            }

        } catch (SQLException e) {
            throw new HabitableBuildingException("Problem with connection", e);
        }

    }

    @Override
    public HabitableBuilding SetToHabitableBuilding(ResultSet resultSet) throws SQLException {
        HabitableBuilding building = new HabitableBuilding();
        building.setCurrentInhabitants(resultSet.getInt("CurrentInhabitants"));
        building.setMaxInhabitants(resultSet.getInt("MaxInhabitants"));
        building.setBuildingsState(resultSet.getBoolean("Active"));
        building.setCoordinates(resultSet.getString("Location"));
        building.setSize(resultSet.getInt("Size"));
        building.setType((HabitableBuildingTypes) resultSet.getObject("Type"));
        return building;
    }

    @Override
    public HabitableBuilding selectFromDBbyLocation(Array location) throws HabitableBuildingException {
        try (Connection connection = dataSource.getConnection()){
            try (PreparedStatement statement = connection.prepareStatement("SELECT * FROM NHabitableBuildings WHERE Coordinates = ?")){
                statement.setArray(1, location);

                ResultSet resultSet = statement.executeQuery();

                if (resultSet.next()){
                    return SetToHabitableBuilding(resultSet);
                }
                else return null;

            } catch (SQLException e) {
                throw new HabitableBuildingException("Problem with connection", e);
            }
        } catch (SQLException e) {
            throw new HabitableBuildingException("Problem with connection", e);
        }
    }

    @Override
    public ArrayList<HabitableBuilding> selectFromDBbyType(HabitableBuildingTypes type) throws HabitableBuildingException {
        ArrayList<HabitableBuilding> output = new ArrayList<>();

        try  (Connection connection = dataSource.getConnection()){
            try(PreparedStatement statement = connection.prepareStatement("SELECT * FROM NonResidentialBuildings WHERE Type = ?")){
                statement.setObject(1, type);

                ResultSet resultSet = statement.executeQuery();

                while (resultSet.next()){
                    output.add(SetToHabitableBuilding(resultSet));
                }
                return output;

            } catch (SQLException e) {
                throw new HabitableBuildingException("Problem with connection", e);
            }
        } catch (SQLException e) {
            throw new HabitableBuildingException("Problem with connection", e);
        }
    }
}
