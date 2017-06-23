// ****************************************************************
// GENERATED FILE -- DO NOT EDIT Unless Response type is not native
// Parameterized with:
//
// EndpointName = index
// RequestName = dataPath
// RequestType = string
// ResponseName = status
// ResponseType = string
// ****************************************************************

package main

import (
	"time"

	"github.com/go-kit/kit/log"
)

type loggingMiddleware struct {
	logger log.Logger
  indexService
}


// Logging decoupled from the service logic
func (mw loggingMiddleware) index(dataPath string) (output string, err error) {
  defer func(begin time.Time) {
    _ = mw.logger.Log(
    "method", "index",
    "input", dataPath,
    // NOTE: Ensure type "string" is printable here
    "output", output,
    "err", err,
    "took", time.Since(begin),
    )
  }(time.Now())

  output, err = mw.indexService.Callindex(dataPath)
  if err != nil {
   
    return "", err
  
  }

  return output, nil
}



