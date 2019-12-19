package org.learning.model;

import org.learning.api.NonResidential;

import java.sql.Array;

public class NonResidentialBuilding implements NonResidential {

    private int max_employees;
    private int current_employees;
    private NonResidentialTypes type;
    private int size;
    private Array coordinates;
    private boolean active;

    @Override
    public int getMaxEmployees() {
        return this.max_employees;
    }

    @Override
    public int getCurrentEmployees() {
        return this.current_employees;
    }

    @Override
    public NonResidentialBuilding setType(NonResidentialTypes TypeOfBuilding) {
        this.type = TypeOfBuilding;
        return this;
    }

    @Override
    public int getSize() {
        return this.size;
    }

    public NonResidentialBuilding setMaxEmployees(int max_employees) {
        this.max_employees = max_employees;
        return this;
    }

    public NonResidentialBuilding setCurrentEmployees(int current_employees) {
        this.current_employees = current_employees;
        return this;
    }

    public NonResidentialBuilding setSize(int size) {
        this.size = size;
        return this;
    }

    public NonResidentialBuilding setCoordinates(Array coordinates) {
        this.coordinates = coordinates;
        return this;
    }

    public NonResidentialBuilding setActive(boolean active) {
        this.active = active;
        return this;
    }

    @Override
    public Array getCoordinates() {
        return this.coordinates;
    }

    @Override
    public boolean getBuildingsState() {
        return this.active;
    }

    @Override
    public boolean validateBuilding() {
        return this.type != null && this.coordinates != null && this.size != 0 && !(this.max_employees < 0);
    }

    @Override
    public NonResidentialTypes getType() {
        return this.type;
    }
}
