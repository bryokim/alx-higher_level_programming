#!/usr/bin/node

exports.addMeMaybe = (number, func) => {
  func(++number);
};
