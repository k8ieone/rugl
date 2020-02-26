package org.learning;

import org.learning.api.NonResidentialBuildingManager;
import org.learning.model.NonResidentialBuilding;
import org.learning.model.NonResidentialBuildingException;
import org.learning.model.NonResidentialTypes;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Lazy;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;

@RestController
@RequestMapping("/main")
public class MainEndpoint {

    @Autowired
    @Lazy
    NonResidentialBuildingManager NonHabitableManager;

    @GetMapping("/")
    public ArrayList<NonResidentialBuilding> getNonResidentialBuildings() throws NonResidentialBuildingException {

        NonResidentialBuilding building0 = new NonResidentialBuilding(10, 5, NonResidentialTypes.POWERLINE, 5, "smt0", true);
        NonResidentialBuilding building1 = new NonResidentialBuilding(14, 9, NonResidentialTypes.FACTORY, 5, "smt1", true);
        NonResidentialBuilding building2 = new NonResidentialBuilding(26, 26, NonResidentialTypes.POWERPLANT, 5, "smt2", true);
        NonResidentialBuilding building3 = new NonResidentialBuilding(31, 24, NonResidentialTypes.FIREHOUSE, 5, "smt3", true);

        NonHabitableManager.addToDB(building0);
        NonHabitableManager.addToDB(building1);
        NonHabitableManager.addToDB(building2);
        NonHabitableManager.addToDB(building3);

        ArrayList<NonResidentialBuilding> listofbuildings = new ArrayList<>();
        listofbuildings.add(NonHabitableManager.selectFromDBbyLocation("smt0"));
        listofbuildings.add(NonHabitableManager.selectFromDBbyLocation("smt1"));
        listofbuildings.add(NonHabitableManager.selectFromDBbyLocation("smt2"));
        listofbuildings.add(NonHabitableManager.selectFromDBbyLocation("smt3"));

        return listofbuildings;
    }



}
