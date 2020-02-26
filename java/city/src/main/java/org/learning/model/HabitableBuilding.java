package org.learning.model;

import java.util.Objects;

public class HabitableBuilding implements org.learning.api.Habitable {

    private int max_inhabitants;
    private int current_inhabitants;
    private String coordinates;
    private HabitableBuildingTypes type;
    private boolean active;
    private int size;

    public HabitableBuilding BasicHabitableBuilding(int max_inhabitants, String coordinates, HabitableBuildingTypes type) {
        this.max_inhabitants = max_inhabitants;
        this.current_inhabitants = 0;
        this.coordinates = coordinates;
        this.type = type;
        return this;
    }

    @Override
    public int getMaxInhabitants() {
        return this.max_inhabitants;
    }

    @Override
    public int getCurrentInhabitants() {
        return this.current_inhabitants;
    }

    @Override
    public HabitableBuilding setType(HabitableBuildingTypes TypeOfBuilding) {
        this.type = TypeOfBuilding;
        return this;
    }

    @Override
    public int getSize() {
        return this.size;
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
        if (this.getMaxInhabitants() > 0 && this.getSize() > 0 && this.getCurrentInhabitants() > -1 && this.getCoordinates() != null){
            return false;
        }
        else{
            return true;
        }
    }

    @Override
    public HabitableBuildingTypes getType() {
        return this.type;
    }

    @Override
    public boolean equals(org.learning.api.Habitable o) {

        if (this == o) return true;
        else return this.getMaxInhabitants() == o.getMaxInhabitants() && this.getSize() == o.getSize() && this.getCoordinates() == o.getCoordinates() && this.getType() == o.getType();

        // if (this == o) return true;
        //
        // if (!this.getBuildingsState() && o.getBuildingsState()){
        //     return false;
        // } else if (this.getBuildingsState() && !o.getBuildingsState()){
        //     return true;
        // } else if (this.getSize() > o.getSize()){
        //     return true;
        // } else if (this.getSize() < o.getSize()){
        //     return false;
        // } else if (this.getMaxInhabitants() > o.getMaxInhabitants()){
        //     return true;
        // } else if (this.getMaxInhabitants() < o.getMaxInhabitants()){
        //     return false;
        // } else{
        //     return true;
        // }
    }

    @Override
    public int hashCode() {
        return Objects.hash(current_inhabitants, active, size);
    }


    public HabitableBuilding setMaxInhabitants(int max_inhabitants) {
        this.max_inhabitants = max_inhabitants;
        return this;
    }

    public HabitableBuilding setCurrentInhabitants(int current_inhabitants) {
        this.current_inhabitants = current_inhabitants;
        return this;
    }

    public HabitableBuilding setCoordinates(String coordinates) {
        this.coordinates = coordinates;
        return this;
    }

    public HabitableBuilding setBuildingsState(boolean active) {
        this.active = active;
        return this;
    }

    public HabitableBuilding setSize(int size) {
        this.size = size;
        return this;
    }
}

