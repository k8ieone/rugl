package org.learning.model;

public enum NonResidentialTypes {
    FACTORY {
        @Override
        public String toString() {
            return "FACTORY";
        }
    },

    POWERLINE {
        @Override
        public String toString() {
            return "POWERLINE";
        }
    },

    FIREHOUSE {
        @Override
        public String toString() {
            return "FIREHOUSE";
        }
    },

    CLINIC {
        @Override
        public String toString() {
            return "CLINIC";
        }
    },

    PHARMACY {
        @Override
        public String toString() {
            return "PHARMACY";
        }
    },

    HOSPITAL {
        @Override
        public String toString() {
            return "HOSPITAL";
        }
    },

    POLICESTATION {
        @Override
        public String toString() {
            return "POLICESTATION";
        }
    },

    POWERPLANT {
        @Override
        public String toString() {
            return "POWERPLANT";
        }
    },

    GOVERNMENTBUILDING {
        @Override
        public String toString() {
            return "GOVERNMENTBUILDING";
        }
    }
}