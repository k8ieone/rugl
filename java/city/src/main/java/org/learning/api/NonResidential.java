package org.learning.api;

import org.learning.model.NonResidentialBuilding;
import org.learning.model.NonResidentialTypes;

import java.sql.Array;
import java.util.ArrayList;
import java.util.List;

public interface NonResidential extends Building{
    public int getMaxEmployees();
    public int getCurrentEmployees();
    public NonResidentialBuilding setType(NonResidentialTypes TypeOfBuilding);
    public NonResidentialBuilding setActive(boolean active);
    public NonResidentialBuilding setCoordinates(ArrayList coordinates);
    public NonResidentialBuilding setSize(int size);
    public NonResidentialBuilding setCurrentEmployees(int current_employees);
    public NonResidentialBuilding setMaxEmployees(int max_employees);
    public NonResidentialTypes getType();
}