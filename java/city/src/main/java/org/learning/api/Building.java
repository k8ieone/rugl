package org.learning.api;

import java.sql.Array;

public interface Building{
    public int getSize();
    public Array getCoordinates();
    public String toString();
    public boolean getBuildingsState();
    public boolean validateBuilding();
}