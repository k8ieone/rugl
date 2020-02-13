package org.learning.configuration;

import org.learning.api.NonResidentialBuildingManager;
import org.learning.model.NonResidentialBuilding;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;

@Configuration
public class NonResidentialBuildingsConfiguration {

    @Bean
    public NonResidentialBuildingManager NonResidentialBuildingManager(DataSource dataSource){

        try (Connection conn = dataSource.getConnection()) {

            conn.prepareStatement("CREATE TABLE NonResidentialBuildings ("
                    + "MaxEmployees INT NOT NULL, "
                    + "CurrentEmployees INT NOT NULL, "
                    + "Size INT NOT NULL, "
                    + "Coordinates ARRAY NOT NULL, "
                    + "Type VARCHAR(255) NOT NULL, "
                    + "Active BOOLEAN NOT NULL, "
                    + "UNIQUE KEY Coordinates (Coordinates))").executeUpdate();

            NonResidentialBuildingManager nonResidentialBuildingManager = new NonResidentialBuildingManagerImplementation();

            return new nonResidentialBuildingManager();

        }
        catch(SQLException e){
            System.out.println(e);
        }


}
