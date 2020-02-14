package org.learning.api;

import org.learning.model.HabitableBuilding;
import org.learning.model.HabitableBuildingTypes;

public interface Habitable extends Building {
    public abstract int getMaxInhabitants();
    public abstract int getCurrentInhabitants();
    public HabitableBuilding setType(HabitableBuildingTypes TypeOfBuilding);
    boolean equals(Habitable o);
    public HabitableBuilding setMaxInhabitants(int max_inhabitants);
    public HabitableBuilding setCurrentInhabitants(int current_inhabitants);
    public HabitableBuilding setCoordinates(String coordinates);
    public HabitableBuilding setBuildingsState(boolean active);
    public HabitableBuilding setSize(int size);
    public HabitableBuildingTypes getType();
}