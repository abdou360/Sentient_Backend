package com.example.ar_backend;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.FieldDefaults;

import javax.persistence.*;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "profs")
@FieldDefaults(level = AccessLevel.PRIVATE)
public class UserEntity {
    @Id @GeneratedValue
    long id;
    @Column(nullable = true)
    String name;
}
