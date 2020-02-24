package org.learning.api;

import org.learning.model.NonResidentialBuilding;
import org.learning.model.NonResidentialBuildingException;
import org.learning.model.NonResidentialTypes;

import java.sql.Array;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public interface NonResidentialBuildingManager {

    public void createNonResidentialBuilding(NonResidential building) throws NonResidentialBuildingException;
    public void addToDB(NonResidential building) throws NonResidentialBuildingException;
    public void deleteFromDB(Habitable building) throws NonResidentialBuildingException;
    public NonResidentialBuilding SetToNonResidentialBuilding(ResultSet resultset) throws SQLException;
    public NonResidentialBuilding selectFromDBbyLocation(String location) throws NonResidentialBuildingException;
    public ArrayList<NonResidentialBuilding> selectFromDBbyType(NonResidentialTypes type) throws NonResidentialBuildingException;
}