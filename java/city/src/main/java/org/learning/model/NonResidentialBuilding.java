package org.learning.model;

import org.learning.api.NonResidential;

public class NonResidentialBuilding implements NonResidential {

    private int max_employees;
    private int current_employees;
    private NonResidentialTypes type;
    private int size;
    private String coordinates;
    private boolean active;

    public NonResidentialBuilding(int max_employees, int current_employees, NonResidentialTypes type, int size, String coordinates, boolean active) {
        this.max_employees = max_employees;
        this.current_employees = current_employees;
        this.type = type;
        this.size = size;
        this.coordinates = coordinates;
        this.active = active;
    }

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

    public NonResidentialBuilding setCoordinates(String coordinates) {
        this.coordinates = coordinates;
        return this;
    }

    public NonResidentialBuilding setActive(boolean active) {
        this.active = active;
        return this;
    }

    @Override
    public String getCoordinates() {
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
