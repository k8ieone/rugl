package org.learning.managers;

import org.learning.api.Habitable;
import org.learning.api.NonResidential;
import org.learning.api.NonResidentialBuildingManager;
import org.learning.model.NonResidentialBuilding;
import org.learning.model.NonResidentialBuildingException;
import org.learning.model.NonResidentialTypes;

import javax.sql.DataSource;
import java.sql.*;
import java.util.ArrayList;

public class NonResidentialBuildingsManager implements NonResidentialBuildingManager {

    private DataSource dataSource;

    @Override
    public void createNonResidentialBuilding(NonResidential building) throws NonResidentialBuildingException {

        try (Connection connection = dataSource.getConnection()) {
            try (PreparedStatement statement = connection.prepareStatement("INSERT INTO NonResidentialBuildings (MaxEmployees, CurrentEmployees, Size, Coordinates, Type, Active) VALUES ?, ?, ?, ?, ?, ?")){
                statement.    setInt(1, building.getMaxEmployees());
                statement.    setInt(2, building.getCurrentEmployees());
                statement.    setInt(3, building.getSize());
                statement.  setArray(4, building.getCoordinates());
                statement. setObject(5, building.getType());
                statement.setBoolean(6, building.getBuildingsState());

                statement.executeUpdate();

            } catch (SQLException e) {
                throw new NonResidentialBuildingException("Problem with connection", e);
            }

        } catch (SQLException e) {
            throw new NonResidentialBuildingException("Problem with connection", e);
        }
    }

    @Override
    public void deleteFromDB(Habitable building) throws NonResidentialBuildingException {

        try (Connection connection = dataSource.getConnection()){
            try (PreparedStatement statement = connection.prepareStatement("DELETE FROM NonResidentialBuildings WHERE Coordinates = ?")){
                statement.setArray(1, building.getCoordinates());
                statement.executeUpdate();

            } catch (SQLException e) {
                throw new NonResidentialBuildingException("Problem with connection", e);
            }
        } catch (SQLException e) {
            throw new NonResidentialBuildingException("Problem with connection", e);
        }

    }

    @Override
    public NonResidentialBuilding SetToNonResidentialBuilding(ResultSet resultSet) throws SQLException {
        NonResidentialBuilding building = new NonResidentialBuilding();
        building.setActive(resultSet.getBoolean("Active"));
        building.setCoordinates(resultSet.getArray("Coordinates"));
        building.setCurrentEmployees(resultSet.getInt("CurrentEmployees"));
        building.setMaxEmployees(resultSet.getInt("MaxEmployees"));
        building.setSize(resultSet.getInt("Size"));
        building.setType((NonResidentialTypes) resultSet.getObject("Type"));

        return building;
    }

    @Override
    public NonResidentialBuilding selectFromDBbyLocation(Array location) throws NonResidentialBuildingException {
        try (Connection connection = dataSource.getConnection()){
            try (PreparedStatement statement = connection.prepareStatement("SELECT FROM * NonResidentialBuildings WHERE Coordinates = ?")){
                statement.setArray(1, location);

                ResultSet resultSet = statement.executeQuery();

                if (resultSet.next()){
                    return SetToNonResidentialBuilding(resultSet);
                }
                else return null;

            } catch (SQLException e) {
                throw new NonResidentialBuildingException("Problem with connection", e);
            }
        } catch (SQLException e) {
            throw new NonResidentialBuildingException("Problem with connection", e);
        }
    }

    @Override
    public ArrayList<NonResidentialBuilding> selectFromDBbyType(NonResidentialTypes type) throws NonResidentialBuildingException {
        ArrayList<NonResidentialBuilding> output = new ArrayList<>();

        try  (Connection connection = dataSource.getConnection()){
            try(PreparedStatement statement = connection.prepareStatement("SELECT * FROM NonResidentialBuildings WHERE Type = ?")){
                statement.setObject(1, type);

                ResultSet resultSet = statement.executeQuery();

                while (resultSet.next()){
                    output.add(SetToNonResidentialBuilding(resultSet));
                }
                return output;

            } catch (SQLException e) {
                throw new NonResidentialBuildingException("Problem with connection", e);
            }
        } catch (SQLException e) {
            throw new NonResidentialBuildingException("Problem with connection", e);
        }
    }
}
