package org.learning.managers;

import com.fasterxml.jackson.databind.JsonSerializer;
import org.learning.api.Habitable;
import org.learning.api.NonResidential;
import org.learning.api.NonResidentialBuildingManager;
import org.learning.model.HabitableBuildingException;
import org.learning.model.NonResidentialBuilding;
import org.learning.model.NonResidentialBuildingException;
import org.learning.model.NonResidentialTypes;
import org.springframework.context.annotation.Bean;

import javax.sql.DataSource;
import java.sql.*;
import java.util.ArrayList;

public class NonResidentialBuildingsManagerImplementation implements NonResidentialBuildingManager {

    private DataSource dataSource;

    public NonResidentialBuildingsManagerImplementation(DataSource dataSource){
        this.dataSource = dataSource;
    }

    @Override
    public void createNonResidentialBuilding(NonResidential building) throws NonResidentialBuildingException {

        try (Connection connection = dataSource.getConnection()) {
            try (PreparedStatement statement = connection.prepareStatement("INSERT INTO NonResidentialBuildings (MaxEmployees, CurrentEmployees, Size, Coordinates, Type, Active) VALUES ?, ?, ?, ?, ?, ?")){
                statement.    setInt(1, building.getMaxEmployees());
                statement.    setInt(2, building.getCurrentEmployees());
                statement.    setInt(3, building.getSize());
                statement.  setString(4, building.getCoordinates());
                statement. setString(5, building.getType().toString());
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
    public void addToDB(NonResidential building) throws NonResidentialBuildingException {

        try (Connection connection = dataSource.getConnection()){
            try (PreparedStatement statement = connection.prepareStatement("INSERT INTO NonResidentialBuildings (MaxEmployees, CurrentEmployees, Size, Coordinates, Type, Active) VALUES (?, ?, ?, ?, ?, ?)")){
                statement.    setInt(1, building.getMaxEmployees());
                statement.    setInt(2, building.getCurrentEmployees());
                statement.    setInt(3, building.getSize());
                statement.  setString(4, building.getCoordinates());
                statement. setString(5, building.getType().toString());
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
                statement.setString(1, building.getCoordinates());
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

        String type = resultSet.getString("Type");
        NonResidentialTypes TypeOfBuilding;

        switch(type){
            case "FACTORY":
                TypeOfBuilding = NonResidentialTypes.FACTORY;
                break;

            case "POWERLINE":
                TypeOfBuilding = NonResidentialTypes.POWERLINE;
                break;

            case "FIREHOUSE":
                TypeOfBuilding = NonResidentialTypes.FIREHOUSE;
                break;

            case "CLINIC":
                TypeOfBuilding = NonResidentialTypes.CLINIC;
                break;

            case "PHARMACY":
                TypeOfBuilding = NonResidentialTypes.PHARMACY;
                break;

            case "HOSPITAL":
                TypeOfBuilding = NonResidentialTypes.HOSPITAL;
                break;

            case "POLICESTATION":
                TypeOfBuilding = NonResidentialTypes.POLICESTATION;
                break;

            case "POWERPLANT":
                TypeOfBuilding = NonResidentialTypes.POWERPLANT;
                break;

            case "GOVERNMENTBUILDING":
                TypeOfBuilding = NonResidentialTypes.GOVERNMENTBUILDING;
                break;

            default:
                TypeOfBuilding = null;
        }

        return new NonResidentialBuilding(resultSet.getInt("MaxEmployees"),
                resultSet.getInt("CurrentEmployees"),
                TypeOfBuilding,
                resultSet.getInt("Size"), resultSet.getString("Coordinates"),
                resultSet.getBoolean("Active"));
    }

    @Override
    public NonResidentialBuilding selectFromDBbyLocation(String location) throws NonResidentialBuildingException {
        try (Connection connection = dataSource.getConnection()){
            try (PreparedStatement statement = connection.prepareStatement("SELECT MaxEmployees, CurrentEmployees, Size, Coordinates, Type, Active FROM NonResidentialBuildings WHERE Coordinates = ?")){
                statement.setString(1, location);

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
                statement.setString(1, type.toString());

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
