package org.learning.configuration;

import org.h2.jdbcx.JdbcDataSource;
import org.learning.managers.NonResidentialBuildingsManagerImplementation;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;


@Configuration
public class NonResidentialBuildingsManagerBean {

    DataSource dataSource;

    @Bean
    public NonResidentialBuildingsManagerImplementation nonResidentialBuildingsManagerImplementation(){
        JdbcDataSource ds = new JdbcDataSource();
        ds.setURL("jdbc:h2:mem:test;DB_CLOSE_DELAY=-1;MODE=PostgreSQL");
        ds.setUser("sa");
        ds.setPassword("sa");
        dataSource = ds;

        return new NonResidentialBuildingsManagerImplementation(dataSource);

    }
}
