package org.learning.model;

public class HabitableBuildingException extends Exception{
    public HabitableBuildingException() { super(); }
    public HabitableBuildingException(String message) { super(message); }
    public HabitableBuildingException(String message, Throwable cause) { super(message, cause); }
    public HabitableBuildingException(Throwable cause) { super(cause); }
}
